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

## 🪪 License

MIT License  
