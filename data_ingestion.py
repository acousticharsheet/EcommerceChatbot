from langchain_astradb import AstraDBVectorStore
from langchain_community.llms import Ollama
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import pandas as pd 
import os
from ecommchatbot.data_converter import data_load

load_dotenv()
ASTRA_DB_API_ENDPOINT_KEY = os.getenv("ASTRA_DB_API_ENDPOINT_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE         =  os.getenv("ASTRA_DB_KEYSPACE")

embedding = OllamaEmbeddings(model= "llama3.1" )
def data_ingest(status):
    vector = AstraDBVectorStore(
        api_endpoint=ASTRA_DB_API_ENDPOINT_KEY,
        embedding=embedding,
        collection_name= "ecommchat1",
        token= ASTRA_DB_APPLICATION_TOKEN,
        namespace= ASTRA_DB_KEYSPACE
    )
    storage = status

    if storage == None:
        docs= data_load()
        inserted_id = vector.add_documents(docs)
    else:
        return  vector
    return vector,inserted_id

if __name__ == "main":
    
    vector, inserted_id = data_ingest(None)
    