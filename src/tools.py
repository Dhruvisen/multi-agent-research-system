from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool
import os
from src.logger import setup_logging

logger = setup_logging()

@tool("search_internet")
def search_internet(query: str) -> str:
    """
    Searches the internet for a given query with fallback logic.
    Tries Tavily search first; if it fails or the API key is missing, 
    falls back to DuckDuckGo search.
    """
    # Try Tavily
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if api_key and not api_key.startswith("your_"):
            tavily = TavilySearchResults(k=10)
            results = tavily.run(query)
            if results:
                return str(results)
        else:
            logger.warning("Tavily API Key missing or default, falling back to DuckDuckGo.")
    except Exception as e:
        logger.error(f"Tavily search failed: {str(e)}. Falling back to DuckDuckGo.")
    
    # Fallback to DuckDuckGo
    try:
        ddg = DuckDuckGoSearchRun()
        return ddg.run(query)
    except Exception as e:
        logger.error(f"DuckDuckGo search failed: {str(e)}")
        return "Search failed. Please try again or refine the query."

def get_search_tool():
    """Returns the unified search tool."""
    return search_internet
