# 🤖 OmniAgent AI

> An autonomous AI agent built with **LangGraph** that can search the web, read and write files, execute Python code, and maintain conversation memory.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Live Demo

🔗 **Try the App:** [https://YOUR-APP-NAME.streamlit.app](https://anup-dhungel-omniagent-ai-app-ufn8ob.streamlit.app/)

---

## 📂 GitHub Repository

🔗 https://github.com/YOUR_USERNAME/OmniAgent-AI

---

# 📖 Overview

OmniAgent AI is an autonomous AI assistant that intelligently chooses the appropriate tool to solve user requests. It integrates Large Language Models (LLMs) with external tools such as web search, Python code execution, and file operations to complete multi-step tasks.

---

# ✨ Features

- 🌐 Real-time Web Search using Tavily Search
- 💻 Execute Python code
- 📄 Read files
- 📝 Create and write files
- 🧠 Conversation memory
- 🤖 Autonomous tool selection with LangGraph
- ⚡ Powered by Groq/OpenAI LLM
- 🎨 Interactive Streamlit interface

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | AI Agent Workflow |
| LangChain | LLM Framework |
| Groq/OpenAI | Large Language Model |
| Tavily Search | Web Search |
| Streamlit | Web Interface |
| Python REPL | Code Execution |
| File I/O | Read & Write Files |

---

# 🏗 Architecture

```
               User
                 │
                 ▼
          Streamlit UI
                 │
                 ▼
          LangGraph Agent
      ┌─────────┼──────────┐
      │         │          │
      ▼         ▼          ▼
 Web Search  Python REPL  File I/O
      │         │          │
      └─────────┼──────────┘
                ▼
          Groq/OpenAI LLM
                │
                ▼
          Final Response
```

---

# 📂 Project Structure

```
OmniAgent-AI/
│
├── app.py
├── main.py
├── agent.py
├── tools.py
├── requirements.txt
├── .env.example
├── README.md
├── .gitignore
│
├── uploads/
├── outputs/
└── memory/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OmniAgent-AI.git
cd OmniAgent-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# 💬 Example Prompts

### 🌐 Web Search

```
Latest AI news today
```

### 📄 Read File

```
Read sample.txt
```

### 📝 Create File

```
Create a file named nepal.py with an introduction to Nepal.
```

### 💻 Execute Code

```
Write Python code to print the Fibonacci series.
```

---


---

# 🔮 Future Improvements

- ✅ RAG Support
- ✅ PDF Upload
- ✅ ChromaDB Integration
- ✅ PostgreSQL Memory
- ✅ Voice Assistant
- ✅ Image Understanding
- ✅ Docker Support
- ✅ Multi-Agent Workflow

---

# 👨‍💻 Author

**Anup**

Aspiring AI/ML Engineer from Nepal 🇳🇵

- GitHub: https://github.com/Anup_Dhungel
- LinkedIn: https://linkedin.com/in/Anup_Dhungel

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub!

---

