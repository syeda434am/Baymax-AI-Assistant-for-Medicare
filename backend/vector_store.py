# backend/vector_store.py
from langchain_community.vectorstores import FAISS
from .embeddings import get_embedding_model
from .document_loader import load_pdf_files
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_vector_store(data_path, db_faiss_path):
    """
    Create and save vector store from PDF documents
    
    Args:
        data_path (str): Path to PDF files
        db_faiss_path (str): Path to save FAISS vector store
    """
    # Load documents
    documents = load_pdf_files(data_path)
    
    # Create text chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    text_chunks = text_splitter.split_documents(documents)
    
    # Get embedding model
    embedding_model = get_embedding_model()
    
    # Create and save FAISS vector store
    db = FAISS.from_documents(text_chunks, embedding_model)
    db.save_local(db_faiss_path)

def load_vector_store(db_faiss_path):
    """
    Load vector store from local FAISS index
    
    Args:
        db_faiss_path (str): Path to FAISS vector store
    
    Returns:
        FAISS: Loaded vector store
    """
    embedding_model = get_embedding_model()
    db = FAISS.load_local(
        db_faiss_path, 
        embedding_model, 
        allow_dangerous_deserialization=True
    )
    return db