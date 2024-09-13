import pandas as pd 
from langchain_core.documents import Document

def data_load():
    print("hi")
    data = pd.read_csv("C:\\Users\\e40068112\\dev\\ECommChatbot\\data\\flipkart_product_review.csv")
    col_data= data[["product_title","review","rating"]]
    product_list=[]
    docs =[]
    for index, data in col_data.iterrows():

        obj = {
            "product_name": data["product_title"],
            "rating"       :data["rating"],
            "review"      : data["review"]  

        }
        
        product_list.append(obj)
    
    for data in product_list:
        metadata= {"product_name" : data["product_name"],
                    "rating"       :data["rating"]}
        doc= Document(page_content= data["review"],metadata=metadata)
        docs.append(doc)
    print ("bi")
    
    return docs

# if __name__ == "main":
#     data_load()