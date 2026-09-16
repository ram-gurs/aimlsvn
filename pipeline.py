import os


import asyncio
from llama_index.core.agent.workflow import ReActAgent

# Core models, settings, and base agent tools
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Query engines and selectors
from llama_index.core.query_engine import (
    RouterQueryEngine, 
    SubQuestionQueryEngine,
    RetrieverQueryEngine
)
from llama_index.core.selectors import LLMSingleSelector
from llama_index.core.question_gen import LLMQuestionGenerator

# Core Agent Framework
from llama_index.core.agent import ReActAgent

# Retrievers and postprocessors
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core.postprocessor import LLMRerank

# Evaluation metrics
from llama_index.core.evaluation import FaithfulnessEvaluator, AnswerRelevancyEvaluator

def run_step_3_naive(indexes, query):
    all_nodes = []
    for idx in indexes.values():
        all_nodes.extend(idx.docstore.docs.values())
    combined_index = VectorStoreIndex(all_nodes)
    query_engine = combined_index.as_query_engine(similarity_top_k=3)
    return query_engine.query(query)

def run_step_4_router(indexes, query):
    tools = [
        QueryEngineTool(
            query_engine=indexes["10-K"].as_query_engine(),
            metadata=ToolMetadata(name="doc_10k_tool", description="Contains FY2024 financials and debt covenants.")
        ),
        QueryEngineTool(
            query_engine=indexes["call"].as_query_engine(),
            metadata=ToolMetadata(name="call_tool", description="Contains Q3 earnings call transcript details.")
        ),
        QueryEngineTool(
            query_engine=indexes["policy"].as_query_engine(),
            metadata=ToolMetadata(name="policy_tool", description="Contains internal risk policy liquidity floors.")
        )
    ]
    
    selector = LLMSingleSelector.from_defaults(llm=Settings.llm)
    router_engine = RouterQueryEngine(selector=selector, query_engine_tools=tools)
    return router_engine.query(query)

def run_step_5_decomposition(indexes, query):
    tools = [
        QueryEngineTool(
            query_engine=indexes[k].as_query_engine(),
            metadata=ToolMetadata(
                name=f"doc_{k.replace('-', '_')}_tool", 
                description=f"Information source for document {k}"
            )
        ) for k in indexes
    ]
    
    # Explicitly supply the core LLMQuestionGenerator to bypass OpenAI requirement
    question_gen = LLMQuestionGenerator.from_defaults(llm=Settings.llm)
    
    sub_engine = SubQuestionQueryEngine.from_defaults(
        question_gen=question_gen,
        query_engine_tools=tools,
        llm=Settings.llm
    )
    return sub_engine.query(query)




from llama_index.core.agent.workflow import ReActAgent


async def run_step_6_agent(indexes, query):
    tools = [
        QueryEngineTool(
            query_engine=indexes[k].as_query_engine(),
            metadata=ToolMetadata(
                name=f"doc_{k.replace('-', '_')}_tool",
                description=f"Detailed context from document {k}",
            ),
        )
        for k in indexes
    ]

    agent = ReActAgent(
        tools=tools,
        llm=Settings.llm,
        verbose=False,
        system_prompt=(
            "You are a financial research agent. "
            "Use the available document tools to answer the user's question. "
            "Use evidence from the supplied documents. "
            "Do not invent financial figures, dates, or policy thresholds."
        ),
    )

    response = await agent.run(user_msg=query)

    return response




def run_step_7_hybrid(indexes, query):
    retrievers = [indexes[k].as_retriever(similarity_top_k=2) for k in indexes]
    fusion_retriever = QueryFusionRetriever(
        retrievers,
        similarity_top_k=3,
        mode="reciprocal_rerank",
        use_async=False
    )
    engine = RetrieverQueryEngine.from_args(fusion_retriever)
    return engine.query(query)

def run_step_8_rerank(indexes, query):
    retriever = indexes["10-K"].as_retriever(similarity_top_k=5)
    reranker = LLMRerank(top_n=1, choice_batch_size=5, llm=Settings.llm)
    engine = RetrieverQueryEngine.from_args(retriever, node_postprocessors=[reranker])
    return engine.query(query)

def run_step_9_hybrid_rerank(indexes, query):
    retrievers = [indexes[k].as_retriever(similarity_top_k=2) for k in indexes]
    fusion_retriever = QueryFusionRetriever(
        retrievers,
        similarity_top_k=4,
        mode="reciprocal_rerank",
        use_async=False
    )
    reranker = LLMRerank(top_n=2, llm=Settings.llm)
    engine = RetrieverQueryEngine.from_args(fusion_retriever, node_postprocessors=[reranker])
    return engine.query(query)

def run_step_10_evaluation(indexes, query):
    engine = indexes["10-K"].as_query_engine()
    response = engine.query(query)
    
    # Explicitly bound global LLM settings to evaluators
    faithfulness = FaithfulnessEvaluator(llm=Settings.llm)
    relevancy = AnswerRelevancyEvaluator(llm=Settings.llm)
    
    f_result = faithfulness.evaluate_response(response=response)
    r_result = relevancy.evaluate_response(query=query, response=response)
    
    return response, f_result, r_result