import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Document

def load_documents_and_build_indexes(data_dir="data"):
    doc_files = {
        "10-K": "10k_excerpt.txt",
        "call": "q3_earnings_call.txt",
        "policy": "internal_risk_policy.txt"
    }
    
    documents = {}
    indexes = {}
    
    for name, filename in doc_files.items():
        filepath = os.path.join(data_dir, filename)
        reader = SimpleDirectoryReader(input_files=[filepath])
        docs = reader.load_data()
        for d in docs:
            d.metadata["source_doc"] = name
        documents[name] = docs
        indexes[name] = VectorStoreIndex.from_documents(docs)
        
    return documents, indexes