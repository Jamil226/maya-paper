from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from llms import embeddings
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

# Path to local vector store
persist_directory = "./chroma_db"

# Cleanup existing db if it exists (optional, for fresh start)
if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)

# Load and split
loader = TextLoader("knowledge_base.json", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Create and persist vector store
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=persist_directory
)

print(f"Ingested {len(chunks)} chunks into {persist_directory}")