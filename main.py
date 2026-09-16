import os
from config import init_models
from data_loader import load_documents_and_build_indexes
import pipeline

def write_markdown_report(step_num, step_title, query, response, extra_info=""):
    os.makedirs("results/lab_runs", exist_ok=True)
    filepath = f"results/lab_runs/step_{step_num:02d}_report.md"
    
    retrieved_chunks_str = ""
    if hasattr(response, 'source_nodes'):
        for node in response.source_nodes:
            src = node.node.metadata.get("source_doc", "Unknown")
            score = f"{node.score:.2f}" if node.score is not None else "N/A"
            text_snippet = node.node.get_content().replace('\n', ' ')
            retrieved_chunks_str += f"- **Source:** {src} | **Score:** {score}\n  - *Excerpt:* {text_snippet}\n"
    
    ans_text = str(response)

    content = f"""# Lab Run Report - Step {step_num}: {step_title}

## Target Query
> {query}

## Retrieved Chunks
{retrieved_chunks_str if retrieved_chunks_str else "No explicit source nodes returned."}

## Model Output Answer
{ans_text}

{extra_info}
"""
    # Added explicit utf-8 encoding to prevent Windows UnicodeEncodeError on special characters
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f" Generated: {filepath}")
    
def main():
    print("Initializing Models and Indexes...")
    init_models()
    documents, indexes = load_documents_and_build_indexes()

    # Step 3
    q3 = "What is the FY2024 revenue, and how does the quick ratio compare to internal policy?"
    r3 = pipeline.run_step_3_naive(indexes, q3)
    write_markdown_report(3, "Naive RAG Baseline", q3, r3)

    # Step 4
    q4 = "What is the mandatory liquidity floor, Q3 ratio, and debt covenants threshold?"
    r4 = pipeline.run_step_4_router(indexes, q4)
    write_markdown_report(4, "RouterQueryEngine", q4, r4)

    # Step 5
    q5 = "How did the quick ratio change over quarters, and does it breach internal policy or debt covenants?"
    r5 = pipeline.run_step_5_decomposition(indexes, q5)
    write_markdown_report(5, "SubQuestion QueryEngine Decomposition", q5, r5)

    # Step 6
    q6 = "Can we open a long position based on our current Q3 quick ratio under the internal risk policy?"
    # r6 = pipeline.run_step_6_agent(indexes, q6)
    r6 =  pipeline.run_step_6_agent(indexes, q6)
    write_markdown_report(6, "Self-Correcting Agent Task", q6, r6)

    # Step 7
    q7 = "How does the quick ratio from earnings call align with internal policy?"
    r7 = pipeline.run_step_7_hybrid(indexes, q7)
    write_markdown_report(7, "Hybrid Search (Dense + Sparse Fusion)", q7, r7)

    # Step 8
    q8 = "What was the gross-margin expansion performance in FY2024?"
    r8 = pipeline.run_step_8_rerank(indexes, q8)
    write_markdown_report(8, "LLMRerank Rescoring", q8, r8)

    # Step 9
    q9 = "Evaluate quick ratio compliance against policy using combined retrieval."
    r9 = pipeline.run_step_9_hybrid_rerank(indexes, q9)
    write_markdown_report(9, "Hybrid Search + Reranking", q9, r9)

    # Step 10
    q10 = "What is the FY2024 Diluted EPS?"
    r10, f_eval, r_eval = pipeline.run_step_10_evaluation(indexes, q10)
    extra_eval_info = f"## Evaluation Results\n- **Faithfulness / Grounding Score:** {f_eval.passing} ({f_eval.score})\n- **Answer Relevancy Score:** {r_eval.passing} ({r_eval.score})"
    write_markdown_report(10, "LLM Evaluation (Faithfulness & Relevancy)", q10, r10, extra_info=extra_eval_info)

if __name__ == "__main__":
    main()