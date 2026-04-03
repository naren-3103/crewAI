from crewai import LLM

# Use llama3.1 as it supports native tool calling which CrewAI requires!
llm = LLM(model="ollama/llama3.1", base_url="http://localhost:11434")
