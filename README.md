# 🤖 Chatbot with LangChain & Groq (LLaMA 3) | Streamlit UI

A lightweight and fast AI chatbot built using **LangChain**, **Groq API (LLaMA3-8B)**, and a **Streamlit web interface**.  
It takes user input, formats it with a structured prompt, invokes Groq-hosted LLM, and returns an intelligent response.

Web page link : 

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

### This is the simple implementation of LangChain and Groq llm to build a basic chatbot, created for practice purpose.
