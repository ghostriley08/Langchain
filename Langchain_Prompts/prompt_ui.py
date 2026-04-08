from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
model = ChatOpenAI(model ="gpt-4o-mini",api_key=os.getenv("GITHUB_TOKEN"),base_url="https://models.inference.ai.azure.com")
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Word2Vec", "Attention is All You Need","GPT-3 Language has few shot learners"],
)
style_input = st.selectbox("Select Style",
                           ["Beginner Friendly","Technical","Code-Oriented","Mathematical"])
length_input = st.selectbox("Select Style",
                           ["Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(detailed explanation)"])

template = load_prompt('template.json')
prompt  = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
   
