# Day 17 – AI Tool Calling

## 📌 Overview

This project demonstrates AI Tool Calling using **Ollama** and the **Llama 3.2** model.

Unlike traditional rule-based programs, the AI model decides which tool to use based on the user's request. The application integrates external Python functions (tools) that the model can invoke dynamically.

---

## 🎯 Objective

The objective of this project is to demonstrate how a Large Language Model (LLM) can intelligently select and execute external tools instead of relying on hardcoded conditions.

---

## 🛠️ Tools

### Calculator Tool
- Evaluates mathematical expressions.
- Examples:
  - `25+8`
  - `(20+30)*5`
  - `150/5`

### Current Time Tool
- Returns the current local system time.

---

## 🏗️ Project Structure

```
Day17_AI_Tool_Calling/
│
├── tools.py
├── main.py
└── README.md
```

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- Function Calling
- Tool Calling

---

## 🔄 Workflow

```
User Question
      │
      ▼
Large Language Model (LLM)
      │
      ▼
Tool Selection
      │
      ▼
Python Tool Execution
      │
      ▼
Tool Result
      │
      ▼
LLM Final Response
```

---

## 💻 Example

### Input

```
What is 25+8?
```

### Tool Selected

```
calculator
```

### Output

```
33
```

---

### Input

```
What time is it?
```

### Tool Selected

```
current_time
```

### Output

```
05:53 PM
```

---
## Screenshots of Code
<img width="950" height="874" alt="image" src="https://github.com/user-attachments/assets/94384032-b407-4384-a419-d7e2ce9f2682" />
<img width="872" height="928" alt="image" src="https://github.com/user-attachments/assets/e45910b2-843c-4df3-83a1-f33ec8b88423" />
<img width="858" height="822" alt="image" src="https://github.com/user-attachments/assets/24aa71f0-45c2-4ce3-8eb2-0cf088d70301" />
<img width="1114" height="460" alt="image" src="https://github.com/user-attachments/assets/aefc26cf-18ad-46a3-a878-063a1bebb5f5" />

## Screenshot of Output
<img width="962" height="886" alt="image" src="https://github.com/user-attachments/assets/b689b07e-fe34-4abf-be79-fe12cfbe4f87" />

## 📚 Learning Outcomes

- Understand AI Tool Calling.
- Integrate Python functions as external tools.
- Allow an LLM to decide which tool to execute.
- Build an intelligent assistant without hardcoded decision logic.

---

## 🚀 Future Improvements

- Add weather and web search tools.
- Integrate OpenAI API.
- Add conversation memory.
- Support multiple tool calls in one interaction.
- Improve error handling and validation.

---

## 👨‍💻 Author

**Mobeen Maroof**
