# Day 20 – Multi-Agent Systems

## Overview

This project demonstrates a simple **Multi-Agent System** consisting of two specialized agents:

- **Researcher Agent**
- **Writer Agent**

Instead of one agent performing every task, the work is divided between specialists. The Researcher Agent gathers structured information, and the Writer Agent converts that information into a readable article. This demonstrates the concept of agent handoff described in the Prompt Engineering Week 3 guide.

---

# Objective

- Design a two-agent workflow.
- Demonstrate information handoff.
- Compare multi-agent and single-agent approaches.

---

# Agent Workflow

```text
User
   │
   ▼
Researcher Agent
   │
   ▼
Structured Data
   │
   ▼
Writer Agent
   │
   ▼
Final Article
```

---

# Agent Responsibilities

## Researcher Agent

- Receives the topic.
- Collects structured information.
- Returns a dictionary containing:
  - Topic
  - Definition
  - Applications

---

## Writer Agent

- Receives structured data.
- Converts it into a readable article.
- Adds a conclusion.

---

# Prototype Demonstration

## Input

Artificial Intelligence

---

## Researcher Output

```python
{
'Topic':'Artificial Intelligence',
'Definition':'AI enables machines to perform tasks that normally require human intelligence.',
'Applications':
[
'Healthcare',
'Education',
'Finance',
'Robotics'
]
}
```

---

## Writer Output

Topic: Artificial Intelligence

Definition:

AI enables machines to perform tasks that normally require human intelligence.

Applications

- Healthcare
- Education
- Finance
- Robotics

Conclusion

This information was prepared by the Writer Agent.

---
## Screenshots Output
<img width="1316" height="886" alt="image" src="https://github.com/user-attachments/assets/9d9b7bae-9734-4bc0-ace7-1b6b3691dc88" />

# Was Splitting into Two Agents Worth It?

For this small project, a single agent could have completed both research and writing. However, separating the tasks makes the workflow easier to understand, test, and extend. In larger systems, specialized agents can improve modularity and maintainability.

---

# Learning Outcome

This exercise demonstrates how multiple specialized agents can collaborate by passing structured information between them. It also highlights that multi-agent systems should only be used when task complexity justifies the additional coordination.
