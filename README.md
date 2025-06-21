🤖 Chatbot with LangChain, Groq (LLaMA 3), and RAG-based Document Retrieval on (ATTENTION.pdf paper)

A lightweight and fast AI chatbot built using **LangChain**, **Groq API (LLaMA3-8B)**, and a **Streamlit web interface**.  
It takes user input, formats it with a structured prompt, invokes Groq-hosted LLM, and returns an intelligent response.

Web page link : https://chatbot-yiojk6aafaxihdccsgfuqi.streamlit.app/

## 📦 Tech Stack

| Tool/Library        | Purpose                               |
|---------------------|---------------------------------------|
|**LangChain**        | Framework to manage LLM flow          |
| **Groq API**        | Inference via ultra-fast LLaMA3-8B    |
| **Streamlit**       | Front-end to interact with chatbot    |
| **Python 3.9**      | Core language                         |
| **LangChain Core**  | Prompt and output pipeline            |
| **LangSmith**       | (Optional) Tracing & monitoring       |
| **Dotenv**          | Load environment variables securely   |

## 🧠 Features

- Uses **LLaMA 3 (8B)** via **Groq’s blazing-fast LPU API**
  
- Clean UI using Streamlit
  
- Structured prompt with `ChatPromptTemplate`
  
- Modular pipeline using LangChain’s chaining
  
- Output parsed as plain text using `StrOutputParser`
  
- Easily extendable with tools, memory, or RAG


## 📚 New: RAG (Retrieval-Augmented Generation)

Integrated RAG-based pipeline to allow chatbot responses using custom documents.

🔍 Key Steps:

  - Ingested content from attention.pdf

  - Split into chunks using LangChain Text Splitter

  - Embedded using Groq-compatible embedding model

  - Stored in Chroma and FAISS vector databases

  - Used retrieval chain to fetch relevant context for user queries

  - Enhanced chatbot responses using custom knowledge base

## 🚀 Summary:

This project combines the power of LangChain, Groq LLM, and RAG architecture. Ideal for learning and extending real-world AI applications.
