# 🤖 AI-Powered Todoist Assistant

A conversational task-management assistant powered by **LangChain**, **Gemini 2.5 Flash**, and the **Todoist API**.  
It allows you to **add tasks**, **view your Todoist list**, and interact naturally through a command-line chat interface.

This project demonstrates how to combine **LLM agents**, **tools**, **APIs**, and **memory** to build intelligent personal assistants.

---

## 🚀 Features

- 🧠 AI-powered conversation using **Gemini 2.5 Flash**
- 📝 Add tasks to Todoist with natural language  
- 📋 Show your Todoist tasks in clean bullet lists  
- 🔁 Maintains conversation history for context  
- 🧩 Custom LangChain tools for task actions  
- 🔐 Secure `.env`-based API key handling  
- 💬 Interactive realtime CLI chat loop  

---

## 🗂️ Project Structure

```
AI_Todoist_Agent/
│
├── main.py              # Main agent script
├── .env                 # API keys (not committed)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🔐 Environment Setup

Create a `.env` file in your project directory:

```env
TODOIST_API_KEY = your_API_goes_here
GEMINI_API_KEY = your_API_goes_here
```

⚠️ Replace the placeholders with your real API keys.  
⚠️ **Do NOT commit your `.env` file.**

---

## 📦 Installation

Install dependencies:

```bash
pip install python-dotenv todoist-api-python langchain langchain-core langchain-google-genai google-generativeai
```

---

## 💻 Full Code (`main.py`)

```python
from dotenv import load_dotenv
import os
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI

load_dotenv()

TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(TODOIST_API_KEY)

@tool
def add_task(task, desc=None):
    """Add a new task to Todoist."""
    todoist.add_task(content=task, description=desc)

@tool
def show_tasks():
    """Return all Todoist tasks."""
    tasks = []
    results_paginator = todoist.get_tasks()
    for batch in results_paginator:
        for task in batch:
            tasks.append(task.content)
    return tasks

tools = [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)

today = datetime.now().strftime("%A, %B %d, %Y")

system_prompt = f"""
You are a helpful AI assistant.
Today's date is: {today}.
You help the user add tasks to Todoist and view their task list.
When showing tasks, format them as a bullet list.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

history = []
while True:
    user_input = input("You: ")
    response = executor.invoke({"input": user_input, "history": history})
    print(response["output"])
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response["output"]))
```

---

## ▶️ Running the Assistant

```bash
python main.py
```

Example:

```
You: Add a task to buy groceries
Assistant: Task added.

You: Show my tasks
Assistant:
• Buy groceries
```

---

## 🧩 Possible Enhancements

- Delete tasks  
- Add labels, projects, priorities  
- Add reminders & due dates  
- Deploy as a web app (FastAPI, Streamlit)  

---

## 🧑‍💻 Author

**Ananthu Prakash**  
📍 Bengaluru, India  
🌐 GitHub: https://github.com/ananthup  
👨‍🏫 Inspired by **Ardit Sulce**

---

## 🪪 License

MIT License  
© 2025 Ananthu Prakash, Ardit Sulce
