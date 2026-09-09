# Day 19 – AI Guardrails Agent

## 📌 Overview

This project demonstrates the implementation of **AI Guardrails** using **Ollama** and the **Llama 3.2** model. The agent safely interacts with external tools while enforcing execution limits, handling tool failures gracefully, and preventing infinite reasoning loops.

The project builds on the ReAct Agent (Day 18) by adding practical safety mechanisms that ensure reliable and controlled AI behavior.

---

## 🎯 Objective

The objective of this project is to design an AI agent with built-in guardrails that:

- Limits the number of reasoning steps.
- Prevents infinite execution loops.
- Handles tool execution errors gracefully.
- Blocks invalid or unsupported tool calls.
- Produces safe and reliable responses.

---

## ✨ Features

- 🤖 AI-powered reasoning using Llama 3.2
- 🛡️ Guardrails for safe execution
- 🔢 Calculator tool
- 🕒 Current time tool
- 🔄 Step limit protection (`MAX_STEPS`)
- ⚠️ Graceful error handling
- 🚫 Unknown tool protection
- 💬 Interactive command-line interface

---

## 📁 Project Structure

```text
Day19_Guardrails/
│
├── main.py
├── guardrails_agent.py
├── tools.py
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- AI Guardrails
- Tool Calling
- ReAct Pattern

---

## 🛡️ Guardrails Implemented

### 1. Maximum Step Limit

The agent limits its reasoning process using a configurable maximum number of reasoning steps.

```python
MAX_STEPS = 5
```

This prevents infinite loops during execution.

---

### 2. Unknown Tool Protection

If the AI requests a tool that is not available, the execution is safely blocked.

Example:

```
Guardrail: Unknown tool blocked.
```

---

### 3. Tool Error Handling

Every tool execution is wrapped inside a `try-except` block to prevent the application from crashing due to runtime errors.

Example:

```
Guardrail: Tool execution failed.
```

---

### 4. Safe Termination

If the maximum reasoning limit is reached, the agent stops execution gracefully.

Example:

```
Guardrail: Maximum reasoning steps reached.
```

---

## 🔄 Workflow

```text
User Question
      │
      ▼
AI Reasoning
      │
      ▼
Guardrail Validation
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
## Screenshots of Code
<img width="988" height="516" alt="image" src="https://github.com/user-attachments/assets/ab12e28e-9b49-419e-85e5-9682b6b072d5" />
<img width="958" height="896" alt="image" src="https://github.com/user-attachments/assets/79323242-356f-487b-85fc-cec69ae2f84f" />
<img width="1032" height="898" alt="image" src="https://github.com/user-attachments/assets/dc1985ea-8498-4b35-8569-66a7340a7aff" />
<img width="1006" height="587" alt="image" src="https://github.com/user-attachments/assets/a2d24b2f-929f-44c2-add2-c85e5f721b1b" />
<img width="925" height="932" alt="image" src="https://github.com/user-attachments/assets/f466e830-bddf-4f28-ab6a-9186ba4c6665" />
<img width="764" height="270" alt="image" src="https://github.com/user-attachments/assets/786f450a-182f-4893-841a-b18105968c84" />

## 🛠️ Available Tools

### Calculator

Performs mathematical calculations.

Example:

```
What is 25 + 8?
```

Output:

```
33
```

---

### Current Time

Returns the current local system time.

Example:

```
What time is it?
```

Output:

```
06:01 PM
```

---

## 💻 Sample Execution

### Input

```
What is 25 + 8?
```

### Output

```
Action      : calculator
Observation : 33

Assistant:
The result of 25 + 8 is 33.
```

---

### Input

```
What time is it?
```

### Output

```
Action      : current_time
Observation : 06:01 PM

Assistant:
The current time is 06:01 PM.
```

---
## Screenshot of Output
<img width="1212" height="910" alt="image" src="https://github.com/user-attachments/assets/eae0e448-f61c-484c-9f98-6a8606d96d31" />


## 📚 Learning Outcomes

Through this project, I learned how to:

- Build AI applications with safety mechanisms.
- Apply guardrails to control LLM behavior.
- Prevent infinite reasoning loops.
- Handle runtime errors safely.
- Integrate external tools with AI models.
- Build reliable AI agents using Python and Ollama.

---

## 🚀 Future Improvements

- Input validation for user queries.
- Logging and monitoring of agent actions.
- Memory support for multi-turn conversations.
- Multiple tool execution in one request.
- Configurable guardrail policies.
- Additional AI tools such as weather, web search, and file processing.

---

## ▶️ Installation

### Install Ollama

Download and install Ollama from the official website.

### Pull the Model

```bash
ollama pull llama3.2
```

### Run the Project

```bash
py main.py
```

---

## 🧪 Sample Questions

```
What is 25+8?

What time is it?

Calculate 25/0

exit
```

---

## 🎓 Key Concepts

- AI Guardrails
- Large Language Models (LLMs)
- ReAct Agents
- Tool Calling
- Safe AI Execution
- Error Handling
- Step Budget
- Responsible AI

---

## 👨‍💻 Author

**Mobeen Maroof**
