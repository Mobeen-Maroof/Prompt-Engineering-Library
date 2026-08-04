# Day 8 – Chain-of-Thought (CoT) Reasoning

## 📌 Objective

The objective of this exercise is to understand how different prompting strategies affect AI reasoning and problem-solving. This activity compares four prompting approaches—No Reasoning, Basic Chain-of-Thought (CoT), Guided CoT, and Structured CoT—using multiple reasoning tasks.

---

# Task 1 – Discount Calculation

## Problem

A shirt costs **$40**. It is discounted by **25%**, then an additional **10% discount** is applied to the discounted price.

---

## No Reasoning Prompt

### Prompt

```
Solve the following problem and provide only the final answer.

A shirt costs $40. It is discounted by 25%, then another 10% discount is applied.
```

### AI Response
<img width="1172" height="651" alt="image" src="https://github.com/user-attachments/assets/668836fa-db7f-4144-83d4-63903d3b701f" />

---

## Basic Chain-of-Thought Prompt

### Prompt

```
Solve the following problem.

Think step by step before giving your final answer.

A shirt costs $40. It is discounted by 25%, then another 10% discount is applied.
```

### AI Response
<img width="1187" height="698" alt="image" src="https://github.com/user-attachments/assets/f97039ba-f3f3-4132-80c5-5de2cb46ad32" />

---

## Guided Chain-of-Thought Prompt

### Prompt

```
Before answering:

1. Identify what is being asked.
2. List the known values.
3. Calculate step by step.
4. Give the final answer.

Problem:

A shirt costs $40. It is discounted by 25%, then another 10% discount is applied.
```

### AI Response
<img width="1121" height="764" alt="image" src="https://github.com/user-attachments/assets/da07f538-203d-4bfd-8ac2-5245af0df22c" />

---

## Structured Chain-of-Thought Prompt

### Prompt

```
Solve this problem using the following format.

Problem Understanding:
Known Values:
Reasoning:
Final Answer:
```

### AI Response
<img width="1102" height="718" alt="image" src="https://github.com/user-attachments/assets/df3d62fc-4e0e-46a0-b24a-fde20fbef841" />

---

# Task 2 – Apple Problem

## Problem

Ali has **18 apples**.

He gives **5** to Sara.

He buys **12** more.

Then he gives **7** to his brother.

How many apples does Ali have?

---

## No Reasoning Prompt

### Prompt

```
Solve the following problem and provide only the final answer.

Ali has 18 apples. He gives 5 to Sara and then buys 12 more. Finally, he gives 7 apples to his brother. How many apples does Ali have now?
```
---
### AI Response
<img width="1086" height="505" alt="image" src="https://github.com/user-attachments/assets/262dd203-74f4-48b4-bfb6-10c5f7758729" />

---
## Basic Chain-of-Thought Prompt

### Prompt

```
Solve the following problem.

Think step by step before giving your final answer.

Ali has 18 apples. He gives 5 to Sara and then buys 12 more. Finally, he gives 7 apples to his brother. How many apples does Ali have now?

```
---
### AI Response
<img width="1176" height="667" alt="image" src="https://github.com/user-attachments/assets/fded7e93-1c80-43a7-8235-0be66d7b70bd" />

---

## Guided Chain-of-Thought Prompt

### Prompt

```
Before answering:

1. Identify what is being asked.
2. List the known values.
3. Calculate step by step.
4. Give the final answer.

Problem:

Ali has 18 apples. He gives 5 to Sara and then buys 12 more. Finally, he gives 7 apples to his brother. How many apples does Ali have now?
```

### AI Response
<img width="1259" height="712" alt="image" src="https://github.com/user-attachments/assets/4223098a-26e5-4db2-b2cd-58cdfef41f57" />

---
## Structured Chain-of-Thought Prompt

### Prompt

```
Solve this problem using the following format.

Problem Understanding:
Known Values:
Reasoning:
Final Answer:
```

### AI Response
<img width="1125" height="754" alt="image" src="https://github.com/user-attachments/assets/ce78aba9-2629-4c2a-a97b-fc0b14df8379" />

---
# Task 3 – Logic Puzzle

## Problem

Ali, Ahmed and Bilal own one pet each.

Ali does not own the dog.

Ahmed does not own the rabbit.

Bilal owns the cat.

Who owns the dog?

---
## No Reasoning Prompt

### Prompt

```
Solve the following problem and provide only the final answer.

Three friends (Ali, Ahmed, and Bilal) each own one pet: a cat, a dog, or a rabbit.

Ali does not own the dog.
Ahmed does not own the rabbit.
Bilal owns the cat.

Who owns the dog?
```
---
### AI Response
<img width="1215" height="667" alt="image" src="https://github.com/user-attachments/assets/b429a6fd-3e8d-4597-9d44-c85176c04bb3" />

---
## Basic Chain-of-Thought Prompt

### Prompt

```
Solve the following problem.

Think step by step before giving your final answer.

Three friends (Ali, Ahmed, and Bilal) each own one pet: a cat, a dog, or a rabbit.

Ali does not own the dog.
Ahmed does not own the rabbit.
Bilal owns the cat.

Who owns the dog?
```
---
### AI Response
<img width="1216" height="740" alt="image" src="https://github.com/user-attachments/assets/a76e10e8-5105-4bc7-9cc5-1e8e3f56c3dd" />

---

## Guided Chain-of-Thought Prompt

### Prompt

```
Before answering:

1. Identify what is being asked.
2. List the known values.
3. Calculate step by step.
4. Give the final answer.

Problem:

Three friends (Ali, Ahmed, and Bilal) each own one pet: a cat, a dog, or a rabbit.

Ali does not own the dog.
Ahmed does not own the rabbit.
Bilal owns the cat.

Who owns the dog?
```

### AI Response
<img width="1255" height="738" alt="image" src="https://github.com/user-attachments/assets/60b71fc3-e358-4b59-a687-153803f091f1" />

---
## Structured Chain-of-Thought Prompt

### Prompt

```
Solve this problem using the following format.

Problem Understanding:
Known Values:
Reasoning:
Final Answer:
```

### AI Response
<img width="1144" height="707" alt="image" src="https://github.com/user-attachments/assets/6293566d-cd09-4871-a845-50b4a8704b58" />

---

# Task 4 – Comparison

## Problem

Which is larger?

7 × (8 + 5)

or

7 × 8 + 7 × 5

---
## No Reasoning Prompt

### Prompt

```
Solve the following problem and provide only the final answer.

Which is larger and why?

7 × (8 + 5)

or

7 × 8 + 7 × 5
```
---
### AI Response
<img width="1315" height="709" alt="image" src="https://github.com/user-attachments/assets/187763a6-9d12-423d-980a-001d474e00f5" />


---
## Basic Chain-of-Thought Prompt

### Prompt

```
Solve the following problem.

Think step by step before giving your final answer.

Which is larger and why?

7 × (8 + 5)

or

7 × 8 + 7 × 5
```
---
### AI Response
<img width="1034" height="780" alt="image" src="https://github.com/user-attachments/assets/8a43e2dc-af74-4c64-9dde-91a81cb2c6a2" />

---

## Guided Chain-of-Thought Prompt

### Prompt

```
Before answering:

1. Identify what is being asked.
2. List the known values.
3. Calculate step by step.
4. Give the final answer.

Problem:

Which is larger and why?

7 × (8 + 5)

or

7 × 8 + 7 × 5
```

### AI Response
<img width="1120" height="825" alt="image" src="https://github.com/user-attachments/assets/50b783ce-3df2-41a6-a65c-1336b35db230" />

---
## Structured Chain-of-Thought Prompt

### Prompt

```
Solve this problem using the following format.

Problem Understanding:
Known Values:
Reasoning:
Final Answer:
```

### AI Response
<img width="1167" height="759" alt="image" src="https://github.com/user-attachments/assets/2815402e-7728-419d-a4f4-aadc8493dc46" />

---

# Task 5 – Study Planning

## Problem

You have **3 hours**.

Subjects:

Python

Machine Learning

Mathematics

Create a balanced study schedule.

---
## No Reasoning Prompt

### Prompt

```
Solve the following problem and provide only the final answer.

You have three hours to study for an exam.

Subjects:
Python
Machine Learning
Mathematics

Create a balanced study schedule.
```
---
### AI Response
<img width="1138" height="762" alt="image" src="https://github.com/user-attachments/assets/62c6c470-373d-465b-8020-34349d602bea" />

---
## Basic Chain-of-Thought Prompt

### Prompt

```
Solve the following problem.

Think step by step before giving your final answer.

You have three hours to study for an exam.

Subjects:
Python
Machine Learning
Mathematics

Create a balanced study schedule.
```
---
### AI Response
<img width="1143" height="682" alt="image" src="https://github.com/user-attachments/assets/5ceb62d4-39b5-4e80-b4f2-65ad9652ede2" />

---

## Guided Chain-of-Thought Prompt

### Prompt

```
Before answering:

1. Identify what is being asked.
2. List the known values.
3. Calculate step by step.
4. Give the final answer.

Problem:

You have three hours to study for an exam.

Subjects:
Python
Machine Learning
Mathematics

Create a balanced study schedule.
```

### AI Response
<img width="1180" height="793" alt="image" src="https://github.com/user-attachments/assets/478e0130-6f9b-4aa6-b16f-72e91a13e616" />

---
## Structured Chain-of-Thought Prompt

### Prompt

```
Solve this problem using the following format.

Problem Understanding:
Known Values:
Reasoning:
Final Answer:
```

### AI Response
<img width="1147" height="772" alt="image" src="https://github.com/user-attachments/assets/b7fbfdaf-151c-422c-9801-7f09c29af6ed" />

---

# Results

| Problem | No Reasoning | Basic CoT | Guided CoT | Structured CoT | Best |
|----------|--------------|-----------|------------|----------------|------|
| Discount | ✅ | ✅ | ✅ | ✅ | Structured |
| Apples | ✅ | ✅ | ✅ | ✅ | Guided |
| Logic | ⚠️ | ✅ | ✅ | ✅ | Guided |
| Comparison | ✅ | ✅ | ✅ | ✅ | Structured |
| Planning | Basic | Better | Better | Best | Structured |

---

# Observation

For simple mathematical problems, all prompting techniques produced correct answers. However, Guided and Structured Chain-of-Thought generated clearer reasoning and better-organized responses, making them more suitable for logic and planning tasks.

---

# Conclusion

This exercise demonstrated that Chain-of-Thought prompting improves the quality and clarity of AI responses for multi-step reasoning tasks. Guided and Structured CoT were especially effective because they organized the reasoning process before presenting the final answer, resulting in more reliable and understandable solutions.

---

# Skills Learned

- Chain-of-Thought Prompting
- Guided Reasoning
- Structured Prompt Design
- Multi-step Problem Solving
- Logical Reasoning with AI
- Prompt Evaluation
- AI Response Analysis
---
