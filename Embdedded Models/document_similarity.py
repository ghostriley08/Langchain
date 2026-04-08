from langchain_huggingface import HuggingFaceEndpointEmbeddings,HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
documents = [
    "New Delhi is the capital of India",
    "Virat Kohli is one of the best cricketers in the world",
    "Artificial Intelligence is transforming modern technology",
    "The Eiffel Tower is located in Paris",
    "Python is a popular programming language for data science"
]

query = "Tell me about Virat Kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

print(scores)
print(documents[np.argmax(scores)])