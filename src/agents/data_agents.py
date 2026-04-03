from crewai import Agent
from src.tools.custom_tools import DataScienceTools
from src.config.llm_config import llm

class DataScienceAgents:

    def data_researcher(self):
        return Agent(
            role='Senior Data Science Researcher',
            goal='Uncover cutting-edge developments, papers, and trends in Data Science.',
            backstory=(
                "You are an expert researcher in the field of Data Science and Artificial Intelligence. "
                "You have a keen eye for identifying new trends, algorithms, and methodologies. "
                "You are thorough and always back up your claims with accurate information."
            ),
            tools=[DataScienceTools.search_internet],  # 1 Tool
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def data_analyst_and_writer(self):
        return Agent(
            role='Lead Data Science Analyst and Technical Writer',
            goal='Analyze research findings and synthesize them into comprehensive, actionable reports.',
            backstory=(
                "You are a seasoned data scientist and technical writer. "
                "You excel at taking complex research data, filtering out the noise, and "
                "creating beautifully structured, easy-to-understand reports. You save your final findings to disk."
            ),
            tools=[DataScienceTools.search_internet],  # Uses search tool for fact checking
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
