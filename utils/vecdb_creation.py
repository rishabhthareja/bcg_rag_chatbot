from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
import os

# Creating the chroma vector db using open AI embeddings
def create_chroma_db(md_header_splits, persist_dir="./chroma_db"):
    documents = [Document(page_content=chunk['content'], metadata=chunk['metadata']) for chunk in md_header_splits]
    return Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory=persist_dir)

# If chroma vector db already exits this code will load 
# exisiting vector db for retrival and generation of response
def load_chroma_db(persist_dir="./chroma_db"):
    return Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
