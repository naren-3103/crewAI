# CrewAI Data Science Project Setup Walkthrough

Congratulations on setting up your first production-ready CrewAI project! Here is a summary of what we accomplished and how you can run the different components.

## Project Structure
The repository is perfectly structured, fully decoupled, and git-friendly:
- `requirements.txt`: Project dependencies including Langchain and FastAPI tools.
- `.gitignore`: Ignoring the virtual environment, cache files, and the `output` repository.
- `src/config/llm_config.py`: Local LLM configuration via LangChain pointing to Ollama.
- `src/tools/custom_tools.py`: Data science tools (Web Search and File Writer).
- `src/agents/data_agents.py`: Declarations for your Single-Tool Researcher and Multi-Tool Analyst.
- `src/tasks/data_tasks.py`: Specific task descriptions assigning duty boundaries for agents.

## Running the Applications

Before running any script, make sure your virtual environment is active:
```powershell
.\venv\Scripts\Activate.ps1
```

> [!NOTE]
> Ensure that Ollama is running in the background and that you have pulled the model defined in `src/config/llm_config.py` (e.g., `ollama run llama3`).

### 1. Terminal / CLI Execution
Run the straightforward command line tool:
```powershell
python cli_main.py
```
It will prompt you for a Data Science topic, after which it will display the crew's thought process step-by-step. The final report will be logged to the console and saved in your `output` folder.

### 2. FastAPI (API Execution)
You can expose your CrewAI as a web service. Start the development server using:
```powershell
uvicorn fastapi_main:app --reload
```
Once it's running, you can test the REST endpoint via Swagger UI at `http://127.0.0.1:8000/docs`. By sending a POST request to `/api/research` with a JSON payload `{"topic": "your DS topic"}`, the task is executed efficiently in the background without blocking the request.

### 3. Streamlit (UI Application)
To use a beautiful, interactive web user interface, run:
```powershell
streamlit run streamlit_main.py
```
This application provides an intuitive way for you (or other users) to trigger the Agents. Follow the logs in your terminal while checking the Streamlit application for the final output.

## Code Extensibility

> [!TIP]
> - **Adding more tools:** Simply create a new `@tool` function in `src/tools/custom_tools.py` and append it to the `tools` array of whichever agent needs it.
> - **Switching LLMs:** If you ever get an OpenAI/Anthropic API key, just replace the Ollama import in `src/config/llm_config.py` with `ChatOpenAI`. The entire codebase stays perfectly intact since dependencies are routed through config.
