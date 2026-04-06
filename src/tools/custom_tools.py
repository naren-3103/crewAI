from langchain_community.tools import DuckDuckGoSearchResults
from crewai.tools import tool
import os

@tool("mega_search")
def mega_search(query: str, max_results: int = 5) -> str:
    """Perform one consolidated web search and return the top results in one single response."""
    search = DuckDuckGoSearchResults()
    result = search.run(query)
    return f"MEGA SEARCH RESULTS for '{query}' (top {max_results} results):\n{result}"

@tool("save_report")
def save_report(content: str, filename: str = "report.md") -> str:
    """Useful to save content/reports to a file system. Requires content and filename."""
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Report successfully saved to {filepath}"


class DataScienceTools:
    mega_search = mega_search
    save_report = save_report
