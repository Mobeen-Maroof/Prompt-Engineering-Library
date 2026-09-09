# Day 20 – Multi-Agent System

## 📌 Overview

This project demonstrates a **Multi-Agent AI System** built using **Python**, **Ollama**, and the **Llama 3.2** language model. Instead of relying on a single AI assistant, the application uses two specialized AI agents that collaborate to solve a user's request.

The **Research Agent** gathers information about the given topic, while the **Writer Agent** uses the research findings to generate a clear, structured, and user-friendly final response.

---

## 🎯 Objective

The objective of this project is to understand how multiple AI agents can work together by assigning different responsibilities to each agent. This project demonstrates communication between AI agents and showcases collaborative problem-solving using Large Language Models (LLMs).

---

## ✨ Features

- 🤖 AI-powered Research Agent
- ✍️ AI-powered Writer Agent
- 🔄 Agent-to-Agent communication
- 💬 Interactive command-line interface
- 🦙 Powered by Ollama and Llama 3.2
- 📄 Dynamic response generation
- 🧠 Prompt engineering for specialized agents

---

## 📁 Project Structure

```text
Day20_Multi_Agent/
│
├── main.py
├── agents.py
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- Multi-Agent Systems
- Prompt Engineering
- Artificial Intelligence

---

## 🤖 Agents

### 🔍 Research Agent

**Responsibility**

- Analyze the user’s topic.
- Gather important facts.
- Generate concise research notes.

Example:

```
Input:
Artificial Intelligence
```

Output:

```
Artificial Intelligence is a branch of computer science focused on
creating systems capable of performing tasks that normally require
human intelligence...
```

---
## Screenshot of Output
<img width="1249" height="885" alt="image" src="https://github.com/user-attachments/assets/ac570382-bf2f-438a-9af7-382ba0a0759d" />
<img width="1260" height="878" alt="image" src="https://github.com/user-attachments/assets/3602a67e-e403-4e61-a63e-b4cc9823b8a0" />

### ✍️ Writer Agent

**Responsibility**

- Receive research notes from the Research Agent.
- Organize the information.
- Produce a clear, structured, and easy-to-understand response.

## Screenshot of Output
<img width="1207" height="901" alt="image" src="https://github.com/user-attachments/assets/dc576139-abaa-4057-b211-2dc530afc968" />
<img width="1203" height="886" alt="image" src="https://github.com/user-attachments/assets/cb70c067-5fa5-4805-817a-4be1bde942b4" />
<img width="1174" height="275" alt="image" src="https://github.com/user-attachments/assets/bab39d45-bbdb-4051-8a35-c468d693ed8d" />

---

## 🔄 Workflow

```text
              User
                │
                ▼
        Research Agent (AI)
                │
        Research Notes
                │
                ▼
          Writer Agent (AI)
                │
         Final Response
                │
                ▼
              User
```

---

## 💻 Sample Execution

### User Input

```
Machine Learning
```

### Research Agent Output
<img width="1203" height="865" alt="image" src="https://github.com/user-attachments/assets/663a901c-9398-4fe2-84f8-9cf0850d1578" />
<img width="1188" height="893" alt="image" src="https://github.com/user-attachments/assets/d681f4af-7ef2-4525-bb42-f41788972914" />

### Writer Agent Output
<img width="1211" height="868" alt="image" src="https://github.com/user-attachments/assets/78fbf134-2354-4b2e-9245-9a1360374937" />
<img width="1195" height="884" alt="image" src="https://github.com/user-attachments/assets/b5f2703c-1548-47e6-99b4-f50b27989ce0" />

---

## 🚀 How It Works

1. User enters a topic.
2. The **Research Agent** receives the topic.
3. The Research Agent generates research notes using the AI model.
4. The notes are passed to the **Writer Agent**.
5. The Writer Agent produces the final response.
6. The final response is displayed to the user.

---

## 📚 Learning Outcomes

Through this project, I learned how to:

- Build a Multi-Agent AI system.
- Design specialized AI agents.
- Enable communication between multiple agents.
- Use prompt engineering for different agent roles.
- Build modular AI applications using Python.
- Integrate Ollama with Python applications.

---

## ▶️ Installation

### Install Ollama

Download and install Ollama.

### Pull the Model

```bash
ollama pull llama3.2
```

### Run the Project

```bash
py main.py
```

---

## 🧪 Example Topics

```
Artificial Intelligence

Machine Learning

Climate Change

Python Programming

Cyber Security

Data Science

Blockchain
```

---

## 🔮 Future Improvements

- Add more specialized AI agents.
- Introduce memory for long conversations.
- Enable web search integration.
- Support document analysis.
- Add a GUI using Streamlit or PyQt.
- Allow multiple agents to work simultaneously.

---

## 🎓 Key Concepts

- Multi-Agent Systems
- Artificial Intelligence
- Large Language Models (LLMs)
- Prompt Engineering
- Agent Collaboration
- AI Communication
- Python Programming

---

## 👨‍💻 Author

**Mobeen Maroof**
