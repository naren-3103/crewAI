import os
import sys

# Ensure the src directory is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crewai import Crew, Process
from src.agents.data_agents import DataScienceAgents
from src.tasks.data_tasks import DataScienceTasks

def run_cli():
    print("Welcome to the Data Science CrewAI CLI!")
    topic = input("Enter a Data Science topic to research (e.g., 'RAG evaluation frameworks'): ")
    
    if not topic.strip():
        print("Topic cannot be empty. Exiting.")
        return

    print(f"\nInitializing Crew for topic: '{topic}'...")

    # Initialize Agents and Tasks objects
    agents = DataScienceAgents()
    tasks = DataScienceTasks()

    # Create specific agents
    researcher = agents.data_researcher()
    analyst = agents.data_analyst_and_writer()

    # Create specific tasks
    research_task = tasks.research_topic_task(researcher, topic)
    analysis_task = tasks.analyze_and_report_task(analyst)

    # Form the Crew
    # Using sequential process: Researcher output goes to Analyst
    crew = Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )

    print("\nKicking off the Crew... This may take a few minutes depending on Ollama.")
    result = crew.kickoff()

    print("\n" + "="*50)
    print("CREW EXECUTION COMPLETE")
    print("="*50)
    print("\nFINAL OUTPUT:\n")
    print(result)

if __name__ == "__main__":
    run_cli()
