import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import get_all_tools

def setup_agent():
    # 1. Ensure API keys are set (they should be set in environment variables before running)
    if not os.environ.get("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    if not os.environ.get("TAVILY_API_KEY"):
        raise ValueError("TAVILY_API_KEY environment variable is not set.")

    # 2. Initialize Model
    # Using Llama 3.1 8B via Groq to avoid rate limits on the 70B model
    model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

    # 3. Initialize Memory
    memory = MemorySaver()

    # 4. Create Agent
    tools = get_all_tools()
    agent_executor = create_react_agent(model, tools, checkpointer=memory)
    
    return agent_executor
