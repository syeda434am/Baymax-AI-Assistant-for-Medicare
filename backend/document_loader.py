# backend/document_loader.py
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

def load_pdf_files(data_path):
    """
    Load PDF files from a specified directory
    
    Args:
        data_path (str): Path to the directory containing PDF files
    
    Returns:
        list: Loaded PDF documents
    """
    loader = DirectoryLoader(
        data_path,
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    
    documents = loader.load()
    return documents