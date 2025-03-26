# Baymax AI Medicare Assistant

## Overview
Baymax is an intelligent AI-powered medical document retrieval and query assistant designed to help users extract and understand information from medical PDF documents using advanced natural language processing.

## Project Architecture
- **Frontend**: Streamlit-based interactive web interface
- **Backend**: Modular Python implementation with:
  - Document loading
  - Vector embeddings
  - Retrieval-based Question Answering
- **Model**: Ollama with Medllama2 LLM
- **Vector Database**: FAISS for efficient document retrieval

## Features
- 📄 Load and process medical PDF documents
- 🔍 Semantic search across document contents
- 💬 Interactive chat interface
- 🧠 Retrieval-augmented generation using Ollama
- 📊 Source document tracing

## Prerequisites
- Python 3.8+
- Ollama
- Git

## Technology Stack
- Langchain
- Streamlit
- Ollama
- HuggingFace Embeddings
- FAISS Vector Store

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/baymax-ai-assistant.git
cd baymax-ai-assistant
```

### 2. Install Ollama
- Download from [Ollama Official Website](https://ollama.com/)
- Pull Medllama2 Model
```bash
ollama pull medllama2
```

### 3. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Prepare Vector Database
```bash
python backend/prepare_db.py
```

### 6. Run the Application
```bash
streamlit run frontend/baymax.py
```

## Project Structure
```
baymax-ai-assistant/
│
├── backend/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── prepare_db.py
│   └── retrieval_qa.py
│
├── frontend/
│   └── baymax.py
│
├── data/
│   └── (your medical PDF files)
│
├── vectorstore/
│   └── db_faiss/
│
├── requirements.txt
└── README.md
```

## Configuration
- Modify `backend/retrieval_qa.py` to change:
  - LLM model
  - Prompt template
  - Retrieval parameters

## Adding Documents
- Place medical PDFs in the `data/` directory
- Run `prepare_db.py` to update vector database

## Troubleshooting
- Ensure Ollama is running
- Check PDF file permissions
- Verify virtual environment activation
- Install missing dependencies

## License
[This project is licensed under the Apache License Version 2.0 - see the LICENSE file for details.]

## Acknowledgements
- Ollama API
- FAISS
- Langchain
- Streamlit
- Medllama2
```