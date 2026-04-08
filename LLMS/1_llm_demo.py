import os 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv # important for loading the environment variable

load_dotenv() # loads the key from the .env file
llm = ChatOpenAI(model = 'Phi-4-mini-instruct', api_key=os.getenv("GITHUB_TOKEN"),base_url = "https://models.inference.ai.azure.com")
# Using GitHub's free endpoint Phi-4-mini-instruct to bypass OpenAI's paid API restrictions.
result = llm.invoke("Who is the PM of India")
print(result)

