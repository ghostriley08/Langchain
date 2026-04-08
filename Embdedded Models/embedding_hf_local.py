from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "India is capital of India",
    "Dhoni was a good cricketer",
    "New Delhi is India's capital"
]

vectors = embedding.embed_documents(documents)

print(vectors)