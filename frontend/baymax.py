# frontend/medibot.py
import os
import sys
import streamlit as st

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from backend.vector_store import load_vector_store
from backend.retrieval_qa import create_qa_chain

# Constants
DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"

@st.cache_resource
def get_vectorstore():
    """
    Cached function to load vector store
    
    Returns:
        FAISS: Loaded vector store
    """
    try:
        vectorstore = load_vector_store(DB_FAISS_PATH)
        return vectorstore
    except Exception as e:
        st.error(f"Failed to load vector store: {e}")
        return None

def main():
    """
    Main Streamlit application
    """
    st.title("Ask Chatbot!")
    
    # Initialize session state for messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display previous messages
    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])
    
    # Chat input
    prompt = st.chat_input("Pass your prompt here")
    
    if prompt:
        # Display user message
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role':'user', 'content': prompt})
        
        try:
            # Load vector store
            vectorstore = get_vectorstore()
            
            if vectorstore is None:
                st.error("Failed to load the vector store")
                return
            
            # Create QA chain
            qa_chain = create_qa_chain(vectorstore)
            
            # Get response
            response = qa_chain.invoke({'query': prompt})
            result = response["result"]
            source_documents = response["source_documents"]
            
            # Format response with source documents
            result_to_show = result + "\nSource Docs:\n" + str(source_documents)
            
            # Display assistant response
            st.chat_message('assistant').markdown(result_to_show)
            st.session_state.messages.append({'role':'assistant', 'content': result_to_show})
        
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()