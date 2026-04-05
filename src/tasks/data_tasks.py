from crewai import Task

class DataScienceTasks:

    def research_topic_task(self, agent, topic: str):
        return Task(
            description=(
                f"Conduct comprehensive research on the topic: '{topic}'." 
        "Use the search tool to gather real data. "
        "DO NOT describe tool usage. ACTUALLY CALL the tool."),
            expected_output='A detailed research summary including links or references to key sources, methods, and results.',
            agent=agent,
            human_input=False
        )

    def analyze_and_report_task(self, agent):
        return Task(
            description=(
                "Review the research output provided by the researcher. "
                "Analyze the findings, structure them logically into a formal report format (Executive Summary, Detailed Findings, Conclusion)."
                "Do not add any extra information or details that are not present in the research output. "
            ),
            expected_output='A finalized, well-structured markdown report.',
            output_file='output/research_report.md',
            agent=agent,
            human_input=False
        )
