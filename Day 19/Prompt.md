# Day 19 – Agents that Survive: Stop Conditions, Reflection & Guardrails

## Overview

This project improves the ReAct agent developed on Day 18 by adding guardrails that make the agent safer and more reliable. The agent now limits the number of execution steps, allows only approved tools, includes a reflection step, and stops gracefully when it cannot complete a task.

---

## Objective

- Add a maximum step limit.
- Add a step budget.
- Restrict the agent to approved tools.
- Add a reflection mechanism.
- Demonstrate graceful failure.

---

## Guardrails Implemented

### 1. Maximum Step Limit

The agent stops after five execution steps to prevent infinite loops.

---

### 2. Step Budget

The agent has a fixed execution budget. If the budget is exceeded, execution stops automatically.

---

### 3. Allowed Tools

Only the following tool is permitted:

- Calculator

Any unapproved tool request is rejected.

---

### 4. Reflection

After each action, the agent evaluates whether the task has been completed or if another strategy is needed.

---

## Successful Execution

### Question

Calculate (15 + 25) × 3

### Thought

Use the calculator tool.

### Action

calculator("(15+25)*3")

### Observation

120

### Reflection

The calculation completed successfully.

### Final Answer

120

---

## Screenshots
<img width="819" height="684" alt="image" src="https://github.com/user-attachments/assets/53baf9d0-a161-4631-a471-bc9249c95056" />
<img width="1002" height="889" alt="image" src="https://github.com/user-attachments/assets/58968dce-1bd0-413d-9130-ca0b67142668" />
<img width="1164" height="867" alt="image" src="https://github.com/user-attachments/assets/4dec694d-9b0d-47f3-8034-3b0faef634a1" />
<img width="943" height="845" alt="image" src="https://github.com/user-attachments/assets/c69fc531-555f-465b-9917-4bd815167108" />

## Graceful Failure Example

### Question

Find the square root of happiness.

### Thought

The available tools cannot solve this request.

### Reflection

Stop execution instead of repeating failed attempts.

### Final Result

Stopped gracefully because no suitable tool exists.

---

## Reflection

The most important guardrail in this project was the maximum step limit because it prevents infinite loops and ensures that the agent always terminates safely. Reflection also improves reliability by allowing the agent to recognize when a task cannot be completed using the available tools.

---

## Learning Outcome

This exercise demonstrates that guardrails are essential for building reliable AI agents. By combining execution limits, tool restrictions, and self-reflection, the agent becomes more stable, predictable, and capable of handling failure gracefully.
