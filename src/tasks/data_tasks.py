from crewai import Task

class DataScienceTasks:

    def research_topic_task(self, agent, topic: str):
        return Task(
            description=(
                f"Conduct comprehensive research on the topic: '{topic}'. "
                "Use the search tool to find the most recent and impactful papers, articles, and discussions. "
                "Compile a detailed summary of the main points, innovations, and challenges."
            ),
            expected_output='A detailed research summary including links or references to key sources, methods, and results.',
            agent=agent
        )

    def analyze_and_report_task(self, agent):
        return Task(
            description=(
                "Review the research output provided by the researcher. "
                "Analyze the findings, structure them logically into a formal report format (Executive Summary, Detailed Findings, Conclusion)."
            ),
            expected_output='A finalized, well-structured markdown report.',
            output_file='output/research_report.md',
            agent=agent
        )
