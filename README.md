# CrewAI Data Science Agents 🚀

Welcome to the **CrewAI Data Science Agents** project! This repository contains a production-ready, highly decoupled AI agent architecture, demonstrating how autonomous agents can work collaboratively to solve real-world data science constraints.

---

## 🤖 What is CrewAI?

[CrewAI](https://www.crewai.com/) is a cutting-edge framework designed to orchestrate role-playing, autonomous AI agents. Unlike traditional LLM execution where you query a single model once, CrewAI allows you to define distinct AI "personas", give them specialized tools, and network them together to tackle complex workflows. 

### How it Works:
1. **Agents:** You define agents with specific roles, storylines (backstories), and goals. E.g., a "Senior Researcher" vs. a "Technical Writer".
2. **Tasks:** You assign very specific tasks to those agents, outlining exactly what they need to accomplish and what their expected output should look like.
3. **Tools:** You can equip agents with custom tools. This allows them to search the internet, read local files, query databases, or write to external APIs.
4. **Crew & Process:** Finally, you gather your agents and tasks into a "Crew", and define how they work. In a `sequential` process, the first agent finishes its task and passes its output as context to the next agent down the line.

CrewAI manages the context handoffs, ensures tool-calling schemas are respected, and parses the final results natively!

---

## 🛠️ Project Workflow

This project is built around a specific **Data Science Research and Analysis** workflow.

### The Crew
1. **Agent 1 (Data Researcher):** 
   - **Tool:** Uses the `DuckDuckGo Search` tool.
   - **Task:** Takes a user-provided Data Science topic, scouts the internet for the most cutting-edge, relevant literature and compiles a brief overview of facts.
2. **Agent 2 (Data Analyst):** 
   - **Tool:** No external network tools. Focuses purely on reasoning.
   - **Task:** Reads the raw data supplied by the Researcher, processes it, filters the noise, and outputs a highly polished Markdown report directly to the `output/` directory!

### The Interfaces
To make this repository "production-ready", the system operates using a local open-source LLM (`Ollama` + `llama3.1`). It is fully decoupled from the UI layer, exposing three different ways to interact with the Crew:

1. **Terminal / CLI (`cli_main.py`):** 
   A lightweight terminal wrapper. Run `python cli_main.py`, type your topic, and watch the agents think via the console.
   
2. **FastAPI (`fastapi_main.py`):** 
   An asynchronous API layer. You can start the server (`uvicorn fastapi_main:app`) and trigger research jobs using JSON payloads via HTTP requests, which execute non-blocking in the background.
   
3. **Streamlit UI (`streamlit_main.py`):** 
   A beautiful, user-friendly frontend. Run `streamlit run streamlit_main.py` to get a browser-based UI where non-technical users can interact with the Research Crew.

---

## ⚙️ Setup & Installation

### 1. Requirements
Ensure you have Python installed, as well as [Ollama](https://ollama.com/) running locally.

### 2. Pull the LLM Model
CrewAI natively requires LLMs capable of rigid tool-calling schemas. Make sure to pull `llama3.1`.
```bash
ollama pull llama3.1
```

### 3. Initialize Python Environment
```bash
python -m venv venv
```
Activate it:
- Windows: `.\venv\Scripts\Activate.ps1`
- Mac/Linux: `source venv/bin/activate`

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

Enjoy exploring the possibilities of AI Agent Orchestration!
