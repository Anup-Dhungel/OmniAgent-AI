import os
from langchain_core.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.utilities import PythonREPL
from langchain_core.tools import Tool

# 3. File Tools
@tool
def read_file(filepath: str) -> str:
    """Reads the contents of a file. Provide the absolute or relative path to the file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def write_file(filepath: str, content: str) -> str:
    """Writes content to a file. Provide the absolute or relative path to the file and the content to write."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing file: {e}"

def get_all_tools():
    """Initializes and returns all tools. Call this after environment variables are loaded."""
    tavily_search = TavilySearchResults(max_results=3)
    
    python_repl = PythonREPL()
    repl_tool = Tool(
        name="python_repl",
        description="Executes python code. Use this for math, data analysis, or general python scripting.",
        func=python_repl.run,
    )
    
    return [tavily_search, repl_tool, read_file, write_file]
