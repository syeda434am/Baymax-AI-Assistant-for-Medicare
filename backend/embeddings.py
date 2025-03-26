# backend/embeddings.py
from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Get the embedding model
    
    Args:
        model_name (str, optional): Name of the embedding model. Defaults to MiniLM.
    
    Returns:
        HuggingFaceEmbeddings: Embedding model
    """
    embedding_model = HuggingFaceEmbeddings(model_name=model_name)
    return embedding_model