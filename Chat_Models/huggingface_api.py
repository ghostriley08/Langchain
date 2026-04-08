from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="katanemo/Arch-Router-1.5B",task = "text-generation")
model=ChatHuggingFace(llm=llm)
print(model.invoke("What is the capital of India ?").content)