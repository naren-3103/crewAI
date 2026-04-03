from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.agents.data_agents import DataScienceAgents
from src.tasks.data_tasks import DataScienceTasks
from crewai import Crew, Process

app = FastAPI(title="Data Science CrewAI API", description="API to trigger CrewAI Data Science Agents")

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    message: str
    topic: str

def run_crew_job(topic: str):
    agents = DataScienceAgents()
    tasks = DataScienceTasks()

    researcher = agents.data_researcher()
    analyst = agents.data_analyst_and_writer()

    research_task = tasks.research_topic_task(researcher, topic)
    analysis_task = tasks.analyze_and_report_task(analyst)

    crew = Crew(
        agents=[researcher, analyst],
        tasks=[research_task, analysis_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Run the crew
    try:
        crew.kickoff()
    except Exception as e:
        print(f"Error during crew execution: {e}")

@app.post("/api/research", response_model=ResearchResponse)
async def trigger_research(request: ResearchRequest, background_tasks: BackgroundTasks):
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")
    
    background_tasks.add_task(run_crew_job, request.topic)
    
    return ResearchResponse(
        message="Research job started in the background. Check the 'output' folder later for the report.",
        topic=request.topic
    )

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
