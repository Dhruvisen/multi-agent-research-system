from src.agents import ResearchAgents
from src.tasks import ResearchTasks
from crewai import Agent, Task

def test_agent_creation():
    agents = ResearchAgents()
    researcher = agents.senior_research_analyst()
    assert isinstance(researcher, Agent)
    assert researcher.role == "Senior Research Analyst"

def test_task_creation():
    agents = ResearchAgents()
    tasks = ResearchTasks()
    researcher = agents.senior_research_analyst()
    task = tasks.research_task(researcher, "AI")
    assert isinstance(task, Task)
    assert "AI" in task.description
