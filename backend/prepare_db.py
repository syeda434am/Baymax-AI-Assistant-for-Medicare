# prepare_db.py
import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from backend.vector_store import create_vector_store

# Constants
DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"

def main():
    # Ensure the vectorstore directory exists
    os.makedirs(os.path.dirname(DB_FAISS_PATH), exist_ok=True)
    
    # Create vector store
    create_vector_store(DATA_PATH, DB_FAISS_PATH)
    print(f"Vector store created at {DB_FAISS_PATH}")

if __name__ == "__main__":
    main()