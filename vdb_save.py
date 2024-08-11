"""
This file contain the code to save the data in croma db
"""
from langchain_chroma import Chroma
from langchain_core.documents import Document
from uuid import uuid4
import json

def add_documents_to_vector_store(data, vector_store, persist_directory="./chroma_langchain_db"):
    documents = [
        Document(
            page_content=comment["text"],
            metadata={"metatag": comment["metatag"]},
            id=uuid4().hex
        )
        for comment in data["comments"]
    ]
    
    # Add documents to the vector store
    vector_store.add_documents(documents=documents)

    # Optionally, persist changes to disk
    vector_store.persist(directory=persist_directory)

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
