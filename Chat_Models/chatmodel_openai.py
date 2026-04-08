import os 
from langchain_openai import ChatOpenAI
from  dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model = "gpt-4o-mini" , api_key = os.getenv("GITHUB_TOKEN"),base_url= "https://models.inference.ai.azure.com",temperature=1.5,max_completion_tokens=10)
result = model.invoke("Write something about Cricket")
print(result.content)