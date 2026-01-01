## 🤖 Personal Agentic AI Chatbot (Production Ready)

This project is a **production-ready GenAI application** that implements an **Agentic AI Chatbot** using **LangGraph ReAct Agents**.  
It follows a **modular, scalable architecture** with a **FastAPI backend**, **Streamlit frontend**, and seamless integration of **Groq and OpenAI LLMs** .

The chatbot is capable of **tool-augmented reasoning**, **search-based responses**, and **API-driven communication**, making it suitable for real-world AI applications.
---

## 🚀 Features

- 🧠 **Agentic AI using LangGraph ReAct**
- ⚡ **FastAPI** backend for high-performance APIs
- 🎨 **Streamlit UI** for interactive chat experience
- 🔍 **LangChain tools** for search & reasoning
- 🤖 **Groq / OpenAI LLM integration**
- 🔐 Environment-based secret management
- 🧩 Modular & production-ready architecture

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **UI:** Streamlit
- **LLMs:** Groq, OpenAI
- **Agent Framework:** LangGraph, LangChain
- **Validation:** Pydantic
- **Language:** Python
- **IDE:** VS Code

---

### 🧩 Project Phases

**Phase 1 – AI Agent**
- API key setup (Groq, Tavily)
- LLM and tool configuration
- Agent creation with search capabilities

**Phase 2 – Backend (FastAPI)**
- Pydantic schema validation
- Agent execution via API requests
- Swagger UI for API exploration

**Phase 3 – Frontend (Streamlit)**
- Interactive UI for model selection and prompts
- Backend communication via REST APIs

---

## 📁 Project Setup Guide

This guide provides step-by-step instructions to set up the project environment and run the application locally.  

## 📑 Table of Contents

- Setting Up a Python Virtual Environment
  - Using Pipenv
- Running the Application
- Important Notes

---

## 🧩 Setting Up a Python Virtual Environment

 Using Pipenv

Install Pipenv (if not already installed):
pip install pipenv

Install dependencies:
pipenv install

Activate the virtual environment:
pipenv shell

---


▶️ Running the Application
The project is divided into three phases.

🧠 Phase 1: Create AI Agent
python ai_agent.py

⚙️ Phase 2: Setup Backend with FastAPI
python backend.py

🎨 Phase 3: Setup Frontend with Streamlit
python frontend.py

---

⚠️ Important Notes
Make sure the backend Python script is running in a separate terminal before starting the frontend.
Activate your virtual environment before running any command.
Environment variables (API keys) should be stored in a .env file (not committed to GitHub).

---
