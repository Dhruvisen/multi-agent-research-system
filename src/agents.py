from crewai import Agent, LLM
from src.tools import get_search_tool
import yaml
import os
from src.logger import setup_logging

logger = setup_logging()

class ResearchAgents:
    def __init__(self):
        self.llm = self._setup_llm()
        self.search_tool = get_search_tool()
        
        # Load agent configs
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'agents.yaml')
        with open(config_path, 'r') as f:
            self.agents_config = yaml.safe_load(f)

    def _setup_llm(self):
        """Sets up the LLM based on the provider specified in .env."""
        provider = os.getenv("LLM_PROVIDER", "ollama").lower()
        
        if provider == "groq":
            logger.info("Using Groq LLM provider")
            return LLM(
                model=os.getenv("GROQ_MODEL", "groq/llama3-70b-8192"),
                api_key=os.getenv("GROQ_API_KEY"),
                temperature=0.7
            )
        elif provider == "gemini":
            logger.info("Using Gemini LLM provider")
            return LLM(
                model=f"gemini/{os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')}",
                api_key=os.getenv("GOOGLE_API_KEY"),
                temperature=0.7
            )
        elif provider == "ollama":
            logger.info("Using Ollama LLM provider")
            return LLM(
                model=f"ollama/{os.getenv('OLLAMA_MODEL', 'llama3')}",
                base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                temperature=0.7
            )
        else:
            logger.warning(f"Unknown provider: {provider}, defaulting to Ollama")
            return LLM(model="ollama/llama3")

    def research_analyst(self) -> Agent:
        config = self.agents_config['research_analyst']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            tools=[self.search_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=True
        )

    def information_architect(self) -> Agent:
        config = self.agents_config['information_architect']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def chief_technical_writer(self) -> Agent:
        config = self.agents_config['chief_technical_writer']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
