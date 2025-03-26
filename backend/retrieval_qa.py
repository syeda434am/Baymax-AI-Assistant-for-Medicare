# backend/retrieval_qa.py
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def set_custom_prompt(custom_prompt_template):
    """
    Create a custom prompt template
    
    Args:
        custom_prompt_template (str): Template for prompting
    
    Returns:
        PromptTemplate: Configured prompt template
    """
    prompt = PromptTemplate(
        template=custom_prompt_template, 
        input_variables=["context", "question"]
    )
    return prompt

def load_llm(model_name="medllama2"):
    """
    Load Ollama LLM
    
    Args:
        model_name (str, optional): Name of Ollama model. Defaults to deepseek.
    
    Returns:
        Ollama: Configured LLM
    """
    llm = Ollama(
        model=model_name,
        temperature=0.5
    )
    return llm

def create_qa_chain(vectorstore, model_name="medllama2"):
    """
    Create QA retrieval chain
    
    Args:
        vectorstore (FAISS): Vector store to retrieve from
        model_name (str, optional): Ollama model name
    
    Returns:
        RetrievalQA: Configured QA chain
    """
    CUSTOM_PROMPT_TEMPLATE = """
    Use the pieces of information provided in the context to answer user's question.
    If you dont know the answer, just say that you dont know, dont try to make up an answer. 
    Dont provide anything out of the given context
    Context: {context}
    Question: {question}
    Start the answer directly. No small talk please.
    """
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=load_llm(model_name),
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={'k':3}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
    )
    
    return qa_chain