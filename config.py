import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

def init_models():
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    # Instantiate Anthropic LLM explicitly overriding model and default kwargs
    llm = Anthropic(
        model="claude-sonnet-5",
        api_key=anthropic_key,
        max_tokens=2048,
        additional_kwargs={}  # Prevents LlamaIndex from bubbling up unwanted prompt kwargs
    )
    
    # Local Hugging Face Embeddings
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )
    
    Settings.llm = llm
    Settings.embed_model = embed_model
    return llm, embed_model