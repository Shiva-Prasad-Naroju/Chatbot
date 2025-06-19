import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

# Setting up the environment keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate(
    [
        ('system', "You are a helpful assistant. Please respond to the user queries"),
        ('user', "Question: {question}")
    ]
)

# Streamlit framework
st.title("CHATBOT WITH LANGCHAIN AND GROQ")
input_text = st.text_input("Search the topic")

# Groq AI LLM
llm = ChatGroq(model="llama3-8b-8192")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))




