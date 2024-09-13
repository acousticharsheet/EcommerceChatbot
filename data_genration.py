from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from ecommchatbot.data_ingestion import data_ingest
from langchain_community.llms import Ollama

def data_genration(vstore):
    retriever = vstore.as_retriever(search_kwargs ={"k":3})

    PRODUCT_BOT_TEMPLATE = """You are an ecommerce bot expert in product recommendations and customer querries .
    You anaalyze product title, rating , and reviews to provide accurate and helpful response.
    Ensure your answer are relevant to the topic and refrain from giving the answer which are not related to the context.
    Your response should be crisp , clear, and informative.

    CONTEXT : {context}

    QUESTION : {question}

    Your Answer
    """
    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
    llm = Ollama(model="llama3.1")
    output_parser = StrOutputParser()

    chain = (
                {"context": retriever , "question" : RunnablePassthrough()}
                    |prompt
                    |llm
                    |output_parser
             )
    
    return chain

if __name__ == "__main__":
    vstore = data_ingest("done")
    chain = data_genration(vstore=vstore)

    print (chain.invoke("can you tell me the low cost budget headset"))
