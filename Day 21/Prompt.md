# Day 21 – AI Capstone Agent

## 📌 Overview

The **AI Capstone Agent** is the final project that combines all the concepts learned throughout the AI Agents module into a single application. It integrates **Tool Calling**, **ReAct Reasoning**, **Guardrails**, and a **Multi-Agent System** using **Ollama** and the **Llama 3.2** model.

The application allows the AI to dynamically decide when to use external tools, safely process user requests, collaborate between specialized AI agents, and provide intelligent responses through an interactive command-line interface.

---

## 🎯 Objective

The objective of this capstone project is to build a complete AI Agent that demonstrates:

- AI Tool Calling
- ReAct (Reason + Act) reasoning
- AI Guardrails
- Multi-Agent Collaboration
- Interactive AI conversations

---

## ✨ Features

- 🤖 AI-powered Assistant using Llama 3.2
- 🔧 Dynamic Tool Calling
- 🧠 ReAct (Reason + Act) workflow
- 🛡️ Input validation and Guardrails
- 👥 Research Agent and Writer Agent collaboration
- 💬 Interactive command-line interface
- ⚡ Modular project structure
- 🔄 Real-time AI responses

---

## 📁 Project Structure

```text
Day21_Capstone_AI_Agent/
│
├── main.py
├── react_agent.py
├── agents.py
├── guardrails_agent.py
├── tools.py
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- AI Tool Calling
- ReAct Pattern
- Multi-Agent Systems
- Prompt Engineering

---

## 🛠️ Components

### 🔧 Tool Calling

The AI dynamically selects and executes external tools when required.

Available tools:

- Calculator
- Current Time

Example:

```
What is 25 + 8?
```

Output

```
33
```

---

### 🧠 ReAct Agent

The ReAct Agent follows the Reason → Action → Observation workflow.

Workflow:

```
User Question
      │
      ▼
Reasoning
      │
      ▼
Tool Selection
      │
      ▼
Tool Execution
      │
      ▼
Observation
      │
      ▼
Final AI Response
```

---

### 🛡️ Guardrails

The project includes safety mechanisms to improve reliability.

Implemented guardrails:

- Empty input validation
- Maximum input length validation
- Safe tool execution
- Controlled application flow

Example:

```
Input cannot be empty.
```

---

### 👥 Multi-Agent System

The project contains two specialized AI agents.

#### 🔍 Research Agent

Responsibilities:

- Analyze user topics
- Generate research notes
- Gather useful information

#### ✍️ Writer Agent

Responsibilities:

- Read research notes
- Organize information
- Produce a structured final response

Workflow:

```
User
   │
   ▼
Research Agent
   │
Research Notes
   │
   ▼
Writer Agent
   │
Final Response
```

---

## 💻 Sample Execution

### Calculator
<img width="938" height="393" alt="image" src="https://github.com/user-attachments/assets/63465206-b557-4ec9-adaf-1b2905ec1881" />

### Time
<img width="963" height="475" alt="image" src="https://github.com/user-attachments/assets/c2099256-74de-4e6d-9674-37844fa3d570" />

### Multi-Agent
Research Agent is working...
<img width="1233" height="866" alt="image" src="https://github.com/user-attachments/assets/9d2c20d4-67a8-4bf0-af56-8e75058b8be9" />
<img width="1208" height="913" alt="image" src="https://github.com/user-attachments/assets/c291d0b8-a0dd-4253-ae1f-6126179394f1" />
<img width="1107" height="469" alt="image" src="https://github.com/user-attachments/assets/7c5bee20-c3e7-45d8-8568-1aa9b3f84ee6" />

Writer Agent is writing...
<img width="1237" height="898" alt="image" src="https://github.com/user-attachments/assets/a40bc2fa-14a3-4526-bdcd-88db396250bb" />
<img width="1256" height="896" alt="image" src="https://github.com/user-attachments/assets/5686dd4c-c25c-4538-a4be-fc1d59a193b7" />
<img width="1277" height="918" alt="image" src="https://github.com/user-attachments/assets/e10abcf1-6f2b-46b3-8614-5dab6d6c33ef" />


---

## 🚀 Installation

### 1. Install Ollama

Download and install Ollama.

### 2. Pull the Model

```bash
ollama pull llama3.2
```

### 4. Run the Project

```bash
py main.py
```

---

## 🧪 Example Commands

```
What is 25+8?

What time is it?

research: Artificial Intelligence

research: Cyber Security

research: Climate Change

exit
```

---

## 📚 Learning Outcomes

Through this capstone project, I learned how to:

- Build AI-powered applications using Python.
- Integrate Large Language Models with external tools.
- Implement the ReAct reasoning pattern.
- Design AI Guardrails for safer execution.
- Develop collaborative Multi-Agent Systems.
- Structure modular AI projects.
- Apply prompt engineering for specialized AI agents.

---

## 🔮 Future Improvements

- Add memory for long conversations.
- Integrate web search tools.
- Support PDF and document analysis.
- Add weather and news tools.
- Develop a Streamlit or PyQt graphical interface.
- Connect the application to external APIs.
- Store conversation history in a database.

---

## 🎓 Key Concepts

- Artificial Intelligence
- AI Agents
- Tool Calling
- ReAct
- Multi-Agent Systems
- Prompt Engineering
- Ollama
- Llama 3.2
- Python

---

## 👨‍💻 Author

**Mobeen Maroof**

Data Science Student
