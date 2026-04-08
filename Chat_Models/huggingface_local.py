from langchain_huggingface import HuggingFacePipeline
import os

os.environ['HF_HOME'] = "D:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="sshleifer/tiny-gpt2",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=50,
        do_sample=True
    )
)

print(llm.invoke("What is the capital of India?"))