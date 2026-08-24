# Day 17 – Tool Use

## Overview

This project demonstrates how an AI model can use external tools through function calling. Two tools were implemented:

1. Calculator
2. Current Time

The system follows the Tool Use workflow:

User Question

↓

Tool Selection

↓

Execute Tool

↓

Return Result

---

## Tool 1

### Name

calculator

### Description

Evaluates mathematical expressions provided by the user.

Example

25*8

Result

200

---

## Tool 2

### Name

get_current_time

### Description

Returns the current system time.

---

## Call → Execute → Return Loop

1. User asks a question.
2. The assistant determines which tool is required.
3. The selected tool executes.
4. The result is returned to the user.

---

## Screenshots
<img width="963" height="590" alt="image" src="https://github.com/user-attachments/assets/b9d150c9-9c7b-4f5f-8bab-ec5c5aa400db" />
<img width="841" height="715" alt="image" src="https://github.com/user-attachments/assets/1dc7503f-035d-4799-805a-b38c19dcf846" />
<img width="892" height="715" alt="image" src="https://github.com/user-attachments/assets/aaf4a0d3-38fa-496a-a7ee-6af7d05db3dc" />
<img width="427" height="434" alt="image" src="https://github.com/user-attachments/assets/f12f4030-8c17-4c9a-9558-1c65020711d9" />


## Test Cases

| User Question | Tool Used | Result |
|--------------|-----------|--------|
| What is 25×8? | Calculator | 200 |
| What is 150/5? | Calculator | 30 |
| What time is it? | Current Time | Current Time |
| Calculate (20+30)*5 | Calculator | 250 |
| Hello | None | Greeting |

---

## Broken Tool Description

### Good Description

Returns the current system time whenever the user asks for time.

### Bad Description

Gets information.

Result:

The vague description does not clearly indicate the tool's purpose, making it difficult for an AI system to determine when it should be used.

---

## Conclusion

This exercise demonstrates that tool descriptions act as prompts for AI systems. Clear and specific descriptions improve tool selection, while vague descriptions reduce accuracy and may lead to incorrect tool usage.
