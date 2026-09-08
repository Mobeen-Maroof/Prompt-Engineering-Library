# Day 18 – ReAct AI Agent

## 📌 Overview

This project implements a **ReAct (Reason + Act)** AI Agent using **Ollama** and **Llama 3.2**. Unlike a rule-based chatbot, the agent reasons about the user's request, selects the appropriate tool, executes it, observes the result, and generates a final response.

The project demonstrates the ReAct framework, where the AI combines reasoning with tool usage to solve user queries dynamically.

---

## 🎯 Objective

The objective of this project is to build an AI agent that follows the **ReAct (Reasoning + Acting)** pattern. The model analyzes the user's question, determines whether a tool is required, executes the selected tool, observes the returned result, and then produces the final answer.

---

## 🛠️ Features

- AI-powered reasoning using Llama 3.2
- Dynamic tool selection
- Calculator tool integration
- Current time tool integration
- Interactive command-line interface
- Continuous conversation using a loop
- Automatic observation handling
- Final answer generation by the AI model

---

## 📁 Project Structure

```
Day18_ReAct_Agent/
│
├── main.py
├── react_agent.py
├── tools.py
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- ReAct Pattern
- AI Tool Calling

---

## 🔄 Workflow

```
User Question
      │
      ▼
Reasoning (Thought)
      │
      ▼
Action Selection
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

## 🧠 Available Tools

### Calculator

Performs mathematical calculations.

Example:

```
What is 25 + 8?
```

Output

```
33
```

---

### Current Time

Returns the current system time.

Example

```
What time is it?
```

Output

```
06:34:57 PM
```

---
## Screenshots of Code 
<img width="809" height="477" alt="image" src="https://github.com/user-attachments/assets/0b7a71e7-66f1-4852-950b-de6d51f5d99b" />
<img width="842" height="752" alt="image" src="https://github.com/user-attachments/assets/2e7c4c95-b3c0-4835-9412-241a3680258e" />
<img width="869" height="766" alt="image" src="https://github.com/user-attachments/assets/b3af004d-e5eb-4edc-a39a-54f4eeb191ee" />
<img width="922" height="806" alt="image" src="https://github.com/user-attachments/assets/f9951ff1-3925-44ac-803d-fee5a1426e26" />
<img width="726" height="790" alt="image" src="https://github.com/user-attachments/assets/491b271c-b7be-47a9-a366-f23758393441" />
<img width="804" height="403" alt="image" src="https://github.com/user-attachments/assets/f3a00417-e297-426a-9bed-60c045dcb4e1" />

## Screenshot of Output
<img width="930" height="896" alt="image" src="https://github.com/user-attachments/assets/2543eeca-f94a-4420-96cf-b4659cc35141" />
<img width="757" height="649" alt="image" src="https://github.com/user-attachments/assets/39079b5d-9667-487e-908f-0e38ac31e52a" />


## 💻 Example Execution

### Input

```
What is 150 / 5?
```

### Agent Process

```
Thought
↓

Action
↓

Calculator Tool
↓

Observation
↓

Final Answer
```

### Output

```
Action      : calculator
Observation : 30

Final Answer:
The result of the calculation is 30.
```

---

## 📚 Learning Outcomes

After completing this project, I learned how to:

- Build an AI agent using the ReAct framework.
- Integrate external Python tools with an LLM.
- Allow the model to decide when a tool is required.
- Process observations returned by external tools.
- Generate intelligent responses using AI reasoning.
- Build interactive AI applications using Python.

---

## 🚀 Future Improvements

- Add web search capabilities.
- Integrate weather information.
- Add memory for multi-turn conversations.
- Support multiple tool calls in one request.
- Improve reasoning transparency.
- Add logging and conversation history.

---

## ▶️ Installation

### Install Ollama

Download and install Ollama from the official website.

### Pull the Model

```bash
ollama pull llama3.2
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

---

## 📝 Sample Questions

```
What is 25+8?

What is 150/5?

Calculate (20+30)*5

What time is it?

Tell me the current time.

exit
```

---

## 🎓 Key Concepts

- ReAct (Reason + Act)
- AI Agents
- Tool Calling
- Observation Loop
- Reasoning
- Large Language Models (LLMs)

---

## 👨‍💻 Author

**Mobeen Maroof**

Artificial Intelligence Student

GitHub Learning Journey – AI Agents
