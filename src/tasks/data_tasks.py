from crewai import Task

class DataScienceTasks:

    def research_topic_task(self, agent, topic: str):
        return Task(
            description=(
                f"Conduct thorough research on '{topic}' using the mega_search tool.\n"
                "CALL mega_search exactly once and use the returned content to produce a deep, informative summary.\n"
                "Gather deep insights, trends, statistics, and meaningful context.\n"
                "Focus on concrete data points, numbers, market shifts, historical trends, emerging patterns, and implications.\n\n"
                "CRITICAL OUTPUT RULES (enforce strictly):\n"
                "1. CALL mega_search exactly once.\n"
                "2. After the mega_search result returns, do NOT call any additional tools.\n"
                "3. Return ONLY the final research summary content - nothing else.\n"
                "4. Do NOT include any JSON, function calls, or tool descriptions.\n"
                "5. Do NOT mention tools, parameters, or implementation details.\n"
                "6. Do NOT include phrases like 'Here are the function calls'.\n"
                "7. Do NOT generate code or scripts.\n"
                "8. Use the single returned search result to synthesize the final summary.\n"
                "9. Format: Summary section → References section → Sources section.\n"
                "10. Start directly with the report content (no preamble).\n"
            ),
            expected_output="Clean research summary with Summary, References, and Sources sections. Include detailed insights, statistics, and trend analysis. No JSON, no tool calls, no meta-information.",
            agent=agent
        ) 
    def analyze_and_report_task(self, agent):
        return Task(
            description=(
                "Review the research output provided by the researcher.\n"
                "Structure the findings into a detailed markdown report with these sections:\n"
                "- Summary: Key findings and insights\n"
                "- References: Cited sources and studies\n"
                "- Sources: URLs and references\n\n"
                "Your report should emphasize the body content. Make the Summary and Detailed Findings robust, with deep insights, numbers, trends, and implications.\n"
                "Include multiple evidence points such as employment growth rates, displacement estimates, sector adoption trends, skill impacts, and projected timelines.\n"
                "Provide at least 4 analytical paragraphs or 6 clear bullet points in the main body.\n"
                "References and Sources should support the report, not outweigh it.\n\n"
                "CRITICAL OUTPUT RULES (enforce strictly):\n"
                "1. Output ONLY the markdown report content\n"
                "2. Do NOT include any JSON, function calls, or tool descriptions\n"
                "3. Do NOT include phrases like 'Here are the function calls' or 'Save the report to file system'\n"
                "4. Do NOT mention tools, parameters, or how to save files\n"
                "5. Do NOT add information not present in the research output\n"
                "6. Start directly with the markdown content (no preamble)\n"
                "7. Use proper markdown formatting with headers, subheaders, bullet points, and quantitative detail\n"
            ),
            expected_output='A finalized, well-structured markdown report with Summary, References, and Sources sections. Make the report body deep, insightful, and data-driven. No JSON, no tool calls, no meta-information.',
            output_file='output/research_report.md',
            agent=agent,
            human_input=False
        )
