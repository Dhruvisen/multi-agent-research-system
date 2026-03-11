from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
import os
from src.logger import setup_logging

logger = setup_logging()

class SearchTools:
    @tool("search_internet")
    def search_internet(query: str) -> str:
        """Searches the internet for a given query.
        Tries Tavily first, and falls back to DuckDuckGo if it fails.
        """
        # Try Tavily
        try:
            if os.getenv("TAVILY_API_KEY"):
                tavily = TavilySearchResults(k=10)
                results = tavily.run(query)
                if results:
                    return str(results)
            else:
                logger.warning("Tavily API Key missing, falling back to DuckDuckGo.")
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
    """Returns the unified search tool with fallback logic."""
    return SearchTools.search_internet
