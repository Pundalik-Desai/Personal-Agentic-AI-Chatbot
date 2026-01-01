import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"Looking for .env file at: {dotenv_path}")
print(f".env file exists: {os.path.exists(dotenv_path)}")
load_dotenv(dotenv_path)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Debug prints to verify environment variables
print("GROQ_API_KEY loaded:", GROQ_API_KEY is not None)
print("OPENAI_API_KEY loaded:", OPENAI_API_KEY is not None)
print("TAVILY_API_KEY loaded:", TAVILY_API_KEY is not None)

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

search_tool = TavilySearch(max_results=2, tavily_api_key=TAVILY_API_KEY or "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")

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    tools = [TavilySearch(max_results=2, tavily_api_key=TAVILY_API_KEY or "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")] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools
    )
    
    # Include system_prompt as a SystemMessage
    messages = [SystemMessage(content=system_prompt)] + [HumanMessage(content=msg) for msg in query]
    state = {"messages": messages}
    
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else "No response generated."