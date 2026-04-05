from langchain_community.tools import DuckDuckGoSearchResults
from crewai.tools import tool
import os

class DataScienceTools:
    
    @tool("search_internet")
    def search_internet(query: str) -> str:
        """Search the internet and return real-time results."""
        search = DuckDuckGoSearchResults()
        return search.run(query)

    @tool("Save Report to File")
    def save_report(content: str, filename: str = "report.md") -> str:
        """Useful to save content/reports to a file system. Requires content and filename."""
        # Ensure output dir exists
        os.makedirs("output", exist_ok=True)
        filepath = os.path.join("output", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Report successfully saved to {filepath}"
