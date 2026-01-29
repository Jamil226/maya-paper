from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model='llama3.1', temperature=0)

embeddings = OllamaEmbeddings(model='llama3.1')
