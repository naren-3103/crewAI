import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from src.agents.data_agents import DataScienceAgents
from src.tasks.data_tasks import DataScienceTasks
from crewai import Crew, Process

st.set_page_config(page_title="Data Science CrewAI", page_icon="🧪", layout="wide")

st.title("🧪 Data Science CrewAI Assistants")
st.markdown("Enter a Data Science topic below to kick off a local research and analysis run using Ollama.")

topic = st.text_input("Research Topic", placeholder="e.g., Explain mixture of experts (MoE) in LLMs")

if st.button("Start Crew"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        st.info(f"Initializing Crew for topic: **{topic}** ...")
        
        with st.spinner("Crew is running... Please check your terminal for detailed logs. This may take several minutes."):
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
            
            try:
                result = crew.kickoff()
                st.success("Crew execution completed!")
                
                st.subheader("Final Output")
                st.markdown(str(result))
                
                st.info("The analyst should have also saved a markdown report to the 'output' directory.")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
