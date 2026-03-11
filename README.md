# 🤖 Multi-Agent Research System (MARS)

A production-ready, autonomous research pipeline powered by **CrewAI** and **LangChain**. This system orchestrates multiple AI agents to perform deep research, structured analysis, and technical report writing with **Human-in-the-loop (HITL)** oversight.

---

## 🌟 Key Features

-   **Multi-Agent Collaboration**:
    -   🔍 **Research Analyst**: Scours the web (Tavily/DuckDuckGo) for verified facts.
    -   🏗️ **Information Architect**: Structures findings into Trends, Challenges, and Opportunities.
    -   ✍️ **Chief Technical Writer**: Synthesizes everything into a professional Markdown report.
-   **Open-Source First**: Native support for **Ollama**, **Groq**, and **Gemini**.
-   **Human-in-the-Loop**: System pauses for your input/approval at critical stages.
-   **Resilient Search**: Automatic fallback to DuckDuckGo if Tavily API fails or is unavailable.
-   **Modern Stack**: Built with `uv` for lightning-fast dependency management and `CrewAI` 2026 syntax.

---

## 🛠️ Setup & Installation

This project uses [**uv**](https://github.com/astral-sh/uv) for Python package management.

### 1. Prerequisites
- Install `uv`: 
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- (Optional) Install [Ollama](https://ollama.com/) if you want to run models locally.

### 2. Clone & Initialize
```bash
git clone <your-repo-url>
cd multi-agent-research-system
uv sync
```

### 3. Configuration
Copy the environment template and add your API keys:
```bash
cp .env.example .env
```
Edit `.env` to select your provider (`groq`, `gemini`, or `ollama`) and add the corresponding keys.

---

## 🚀 Running the System

To start a new research project, simply run:

```bash
uv run main.py
```

1.  **Enter Topic**: When prompted, provide your research subject.
2.  **Review & Approve**: The system will pause after the research phase. 
    - Type instructions to refine the search.
    - Press **Enter** (or type "yes/ok") to proceed to writing.

---

## 📁 Project Structure

```text
├── config/
│   ├── agents.yaml      # Personality and goals of agents
│   └── tasks.yaml       # Detailed task requirements
├── src/
│   ├── agents.py        # CrewAI Agent factory
│   ├── tasks.py         # CrewAI Task factory
│   ├── tools.py         # Resilient Search tool
│   └── logger.py        # Production logging
├── main.py              # Orchestration and HITL logic
├── pyproject.toml       # uv project configuration
└── README.md            # You are here
```

---

## 📤 Upload to GitHub

1. Create a new repository on GitHub.
2. Run the following commands:
```bash
git init
git add .
git commit -m "Initial commit: Multi-Agent Research System with HITL and UV"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

---

## ⚖️ License
MIT License. Feel free to use and modify for your own research projects!

---

## 🔮 What's Next (MARS 2.0)
The following enhancements are planned to make the system more robust and user-friendly:

1.  **Streamlit Dashboard**: A professional web interface to replace the CLI.
2.  **API Key Validator**: Proactive checks to catch "Invalid API Key" errors before agents start.
3.  **Model Smart-Switching**: Using `llama3.2:1b` for fast research and a larger model for the final technical writing.
4.  **Vector Memory**: Integrating ChromaDB to allow agents to remember facts across multiple sessions.
5.  **Multi-Format Export**: One-click export of reports to PDF and HTML.
