# Day 21 – Week 3 Capstone Project

## Overview

This project combines everything learned during Week 3 of Prompt Engineering into a single ReAct-style AI agent. The agent can reason about a task, select the appropriate tool, execute the tool, observe the result, reflect on the outcome, and provide a final answer. It also includes guardrails to ensure safe and reliable execution.

---

## Features

- Two working tools:
  - Calculator
  - Current Time
- Thought → Action → Observation workflow
- Reflection after each action
- Maximum step limit
- Allowed tools validation
- Graceful failure handling
- Success and failure execution traces

---

## Project Structure

```text
Day21_Final/
│
├── README.md
├── tools.py
├── agent.py
├── success_trace.txt
└──  failure_trace.txt
```

---

## Example 1 – Successful Execution

**Question**

Calculate (25+15)*4

**Thought**

The user wants to perform a calculation.

**Action**

calculator("(25+15)*4")

**Observation**

160

**Reflection**

The calculation completed successfully.

**Final Answer**

160

---

## Example 2 – Graceful Failure

**Question**

Find the happiness index of dreams.

**Thought**

No suitable tool exists for this task.

**Reflection**

Stop execution instead of entering an infinite loop.

**Final Result**

Unable to complete the request.

---
## Screenshots 
<img width="943" height="827" alt="image" src="https://github.com/user-attachments/assets/4444e3bd-e051-4f5b-844a-a8178514e0cf" />
<img width="818" height="873" alt="image" src="https://github.com/user-attachments/assets/8c178483-3a30-4265-bd4f-b8db2f8afce7" />

## Guardrails

- Maximum execution steps
- Step budget
- Allowed tools only
- Reflection after each action
- Graceful failure for unsupported requests

---

## Learning Outcome

This capstone project demonstrates how prompt engineering concepts can be combined to create a simple but reliable AI agent. By integrating tools, reasoning, guardrails, and reflection, the agent can complete supported tasks and fail safely when a request is beyond its capabilities.

---

## Future Improvements

- Add web search as a third tool.
- Connect the agent to a real LLM API.
- Replace rule-based logic with model-driven tool selection.
- Add Retrieval-Augmented Generation (RAG) support.
