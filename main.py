from dotenv import load_dotenv
import os
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist= TodoistAPI(todoist_api_key)

@tool
def add_task(task, desc=None):
    """
    Add a new taks to the user's task list. 
    Use this when the user wants to use or create a task
    """
    todoist.add_task(content = task, description=desc)

@tool
def show_tasks():
    """
    When the user asks for the todo list show all the tasks from todoist,
    Use this tool when the user wants to see their todo list.
    """
    
    results_paginator = todoist.get_tasks()
    tasks = []
    for task_list in results_paginator:
        for task in task_list:
            tasks.append(task.content)
    return tasks

tools= [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    google_api_key= gemini_api_key,
    temperature= 0.3
)

today = datetime.now().strftime("%A, %B %d, %Y")

system_prompt = f"""
                    You are a helpful assistant.
                    Today's date is: {today}.
                    Use this information to answer questions,
                    You'll help the user add new todo.
                    If the user asks to show todos form todoist then print out the tasks in a bullet list format.
                    """
""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

# chain = prompt | llm | StrOutputParser()
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executer = AgentExecutor(agent=agent, tools = tools, verbose = True)

# response = agent.invoke({"input":user_input})

history = []
while True:
    user_input = input("You: ")
    response = agent_executer.invoke({"input": user_input, "history": history })
    print(response['output'])
    history.append(HumanMessage(content= user_input))
    history.append(AIMessage(content=response['output']))
    