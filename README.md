# 🤖 OmniAgent AI

An autonomous AI agent built with **LangGraph** that can search the web, read files, execute Python code, and maintain conversation memory.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

- 🌐 Web Search using Tavily Search API
- 📄 Read text files
- 💻 Execute Python code safely
- 📂 File Input/Output (Read & Write Files)
- 🧠 Persistent conversation memory
- 🤖 Autonomous tool selection using LangGraph
- ⚡ Powered by Groq/OpenAI LLMs
- 🔧 Modular and extensible architecture

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | AI Agent Workflow |
| LangChain | LLM Integration |
| Groq/OpenAI | Large Language Model |
| Tavily Search | Real-time Web Search |
| Python REPL | Code Execution |
| File I/O | Read & Write Files |

---

## 📂 Project Structure

```
OmniAgent-AI/
│
├── main.py                 # Entry point
├── agent.py                # LangGraph agent
├── tools.py                # Custom tools
├── prompts.py              # System prompts
├── requirements.txt
├── app.py                  # Streamlit UI (if added)
├── README.md
├── .env.example
├── .gitignore
│
├── uploads/
├── outputs/
└── memory/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/OmniAgent-AI.git

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

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Project

Terminal version

```bash
python main.py
```

Streamlit version

```bash
streamlit run app.py
```

---

## 💬 Example Prompts

### Web Search

```
Latest AI news today
```

### File Reading

```
Read sample.txt
```

### File Writing

```
Create a file called nepal.py with an introduction to Nepal.
```

### Code Execution

```
Write Python code to generate Fibonacci numbers.
```

---

## 📸 Demo

Add screenshots or a GIF here.

Example:

```
images/demo.png
```

---

## 🏗️ Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
LangGraph Agent
   │
 ├───────────────┐
 │               │
 ▼               ▼
Tavily      Python REPL
 │               │
 ▼               ▼
Web         File I/O
      │
      ▼
 Groq/OpenAI
```

---

## 📌 Future Improvements

- PDF Reader
- RAG Support
- ChromaDB Integration
- PostgreSQL Memory
- Voice Assistant
- Image Understanding
- Multi-Agent Collaboration
- Docker Deployment
- Authentication
- REST API

---

## 👨‍💻 Author

**Anup**

Aspiring AI/ML Engineer from Nepal.

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
