import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables from .env file
load_dotenv()

# Set Google API key
google_API_key = os.getenv("GOOGLE_API_KEY")

def create_vector_db():
    """
    Creates a vector database using the provided text file.

    Returns:
        vectordb (Chroma): The created vector database.
    """
    try:
        loader = TextLoader("data/knowledge_base.txt", autodetect_encoding=True)
        documents = loader.load()
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=google_API_key)
        vectordb = Chroma.from_documents(documents, embedding=embeddings, persist_directory="chroma_db")
        vectordb.persist()
        return vectordb
    except Exception as e:
        print(f"Error: {e}")

def get_relevant_docs(query):
    """
    Retrieves relevant documents from the vector database based on the query.

    Args:
        query (str): The query to search for.

    Returns:
        results (list): A list of relevant documents.
    """
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=google_API_key)
        vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
        results = vectordb.similarity_search(query, k=2)
        return results
    except Exception as e:
        print(f"Error: {e}")