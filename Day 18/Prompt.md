# Day 18 – ReAct Agent

## Overview

This project demonstrates a simple **ReAct (Reasoning + Acting)** agent. The agent solves a multi-step problem by following the **Thought → Action → Observation** pattern before producing a final answer.

---

## Objective

- Understand the ReAct pattern.
- Reuse tools developed on Day 17.
- Demonstrate a complete reasoning trace.
- Solve a multi-step question.

---

## ReAct Workflow

```text
Question
   ↓
Thought
   ↓
Action
   ↓
Observation
   ↓
Answer
```

---

## Multi-Step Question

**Question**

What is (25 + 15) × 4?

---

### Thought

I need to first add 25 and 15, then multiply the result by 4.

---

### Action

```text
calculator("(25+15)*4")
```

---

### Observation

```text
160
```

---

### Final Answer

The answer is **160**.

---

## Screenshots
<img width="775" height="636" alt="image" src="https://github.com/user-attachments/assets/e630ac1c-cc76-44ce-b2a3-298798607d62" />
<img width="831" height="941" alt="image" src="https://github.com/user-attachments/assets/bf86c073-c8db-46d6-893d-45acf90c8698" />
<img width="941" height="809" alt="image" src="https://github.com/user-attachments/assets/4d21c585-1210-496a-9c06-73a75cc6c354" />

---

## Learning Outcome

This exercise demonstrates how an AI agent can reason before acting. The agent follows a structured process of **Thought → Action → Observation → Answer**, making its decision-making transparent and easier to debug. This pattern forms the foundation of many modern AI agents.
