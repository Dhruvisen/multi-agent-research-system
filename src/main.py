from crewai import Crew, Process
from src.agents import ResearchAgents
from src.tasks import ResearchTasks
from dotenv import load_dotenv
import os
from src.logger import setup_logging

logger = setup_logging()

def main():
    load_dotenv()
    
    # Get user input for the research topic
    print("\n" + "="*50)
    print("      MULTI-AGENT RESEARCH SYSTEM (PROD-v1)")
    print("="*50)
    topic = input("\nEnter the research topic for deep analysis: ").strip()
    
    if not topic:
        logger.error("Empty topic provided.")
        print("Error: Topic cannot be empty.")
        return
    
    logger.info(f"Initializing research crew for topic: {topic}")
    
    # Initialize agents and tasks
    agents = ResearchAgents()
    tasks = ResearchTasks()
    
    # Create agents
    researcher = agents.research_analyst()
    architect = agents.information_architect()
    writer = agents.chief_technical_writer()
    
    # Create tasks
    task1 = tasks.research_task(researcher, topic)
    task2 = tasks.analysis_task(architect, topic)
    task3 = tasks.writing_task(writer, topic)
    
    # Define the crew
    crew = Crew(
        agents=[researcher, architect, writer],
        tasks=[task1, task2, task3],
        process=Process.sequential, 
        verbose=True
    )
    
    # Kick off the process
    print(f"\n### Starting research on: {topic}")
    result = crew.kickoff()
    
    print("\n\n########################")
    print("## FINAL REPORT ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    main()
