# Day 9 – Self-Consistency: Answer Several Times, Then Vote

## Objective

The objective of this exercise is to improve the reliability of AI-generated responses using the **Self-Consistency** prompting technique. Instead of relying on a single reasoning path, the model generates multiple independent answers and selects the most frequent answer using majority voting.

---

#  Introduction

Chain-of-Thought prompting improves reasoning by allowing the model to solve problems step by step. However, a single reasoning path may sometimes lead to an incorrect answer.

Self-Consistency improves reliability by generating multiple reasoning paths for the same problem and selecting the answer that appears most frequently. This technique is similar to ensemble learning in Machine Learning, where multiple predictions are combined to obtain a more reliable result.

---

# Technologies Used

- ChatGPT
- Python
- collections.Counter
- Random Module
- Markdown
- GitHub

---

# Python Implementation

## self_consistency.py

```python
from collections import Counter
import random

responses = {
    "Discount": ["27", "27", "24", "27", "27"],
    "Apple": ["18", "18", "18", "18", "18"],
    "Logic": ["Ahmed", "Ahmed", "Ali", "Ahmed", "Ahmed"],
    "Comparison": ["Equal", "Equal", "Equal", "Equal", "Equal"],
    "Planning": [
        "Python 1h | ML 1h | Math 1h",
        "Python 1h | ML 1h | Math 1h",
        "Math 1h | Python 1h | ML 1h",
        "Python 1h | ML 1h | Math 1h",
        "Python 1h | ML 1h | Math 1h"
    ]
}

def self_consistency(problem):
    samples = random.sample(responses[problem], 5)
    majority = Counter(samples).most_common(1)[0][0]
    return samples, majority

for problem in responses:
    samples, vote = self_consistency(problem)

    print("=" * 40)
    print("Problem:", problem)
    print("Samples:")
    for s in samples:
        print("-", s)
    print("Majority Vote:", vote)
```
---
## AI Response
<img width="1393" height="892" alt="image" src="https://github.com/user-attachments/assets/5d30b16a-8b2e-4c55-a53f-486cab1dacc7" />

---

# Problems Used

## Problem 1

A shirt costs **$40**.

A **25%** discount is applied.

Then another **10%** discount is applied.

Find the final price.

---
## AI Response
<img width="1070" height="817" alt="image" src="https://github.com/user-attachments/assets/5e10a546-acf8-4ceb-861f-57d0ba520a8a" />

---

## Problem 2

Ali has **18 apples**.

He gives **5** to Sara.

He buys **12** more.

Then gives **7** to his brother.

How many apples remain?

---
## AI Response
<img width="1247" height="820" alt="image" src="https://github.com/user-attachments/assets/7003fd0b-1222-49f1-aad0-a0dc1018ad53" />

---
## Problem 3

Ali, Ahmed and Bilal each own one pet.

Ali does not own the dog.

Ahmed does not own the rabbit.

Bilal owns the cat.

Who owns the dog?

---
## AI Response
<img width="1157" height="815" alt="image" src="https://github.com/user-attachments/assets/511be7ed-fa0a-4fc3-9cc4-3a1f3c4da438" />

---
## Problem 4

Which expression is larger?

7 × (8 + 5)

or

7 × 8 + 7 × 5

---
## AI Response
<img width="1103" height="807" alt="image" src="https://github.com/user-attachments/assets/7f8dda32-954f-45cb-b32f-8239a7fc29c7" />

---
## Problem 5

Create a balanced study schedule for

- Python
- Machine Learning
- Mathematics

Total available time:

3 hours.

---
## AI Response
<img width="1128" height="670" alt="image" src="https://github.com/user-attachments/assets/d123fe25-d3bd-4569-ac52-b7764fa64d5a" />
<img width="1174" height="674" alt="image" src="https://github.com/user-attachments/assets/7f9893ce-c56b-4741-8209-3a6fbf28f9bf" />

---
# Results

| Problem | Single CoT | Majority Vote (5 Samples) | Final Result |
|----------|------------|---------------------------|--------------|
| Discount | $27 | $27 | ✅ Correct |
| Apple | 18 | 18 | ✅ Correct |
| Logic | Ahmed | Ahmed | ✅ Correct |
| Comparison | Equal | Equal | ✅ Correct |
| Planning | Balanced Schedule | Balanced Schedule | ✅ Correct |

---

# Accuracy Comparison

| Method | Correct Answers |
|----------|----------------|
| Single CoT | 5 / 5 |
| Self-Consistency | 5 / 5 |

Although both methods produced correct answers in this exercise, Self-Consistency provides greater confidence by reducing the impact of occasional incorrect reasoning paths.

---

# Observation

For numerical and logical reasoning problems, the majority of generated responses converged to the correct answer. Even when one sample produced an incorrect answer, majority voting successfully selected the correct result.

Self-Consistency is particularly useful for complex reasoning tasks where different reasoning paths may produce different outputs.

---

# Cost vs Benefit

Self-Consistency requires multiple AI calls, increasing computational cost and response time. For simple arithmetic problems, this additional cost provides little benefit. However, for complex reasoning, planning, and logical decision-making tasks, majority voting significantly improves confidence in the final answer, making the extra cost worthwhile.

---

# Skills Learned

- Self-Consistency Prompting
- Majority Voting
- Chain-of-Thought Reasoning
- Prompt Engineering
- AI Reliability
- Python Programming
- Counter Collection
- Multi-step Reasoning
- AI Evaluation

---

# Conclusion

This exercise demonstrated that Self-Consistency improves AI reliability by generating multiple independent reasoning paths and selecting the most common answer through majority voting. While the approach increases computational cost, it provides greater confidence and stability for complex reasoning tasks, making it an effective technique in Prompt Engineering.
