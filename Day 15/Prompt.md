# Day 15 – Context Engineering

## Overview

This exercise demonstrates the concept of **Context Engineering**, which focuses on organizing information efficiently so that Large Language Models (LLMs) receive only the most relevant context. The goal is to compare different prompting strategies and determine which one provides the best answer while using the fewest tokens.

---

# Objective

- Understand the importance of context engineering.
- Compare three different prompt strategies.
- Measure approximate token usage.
- Identify the most efficient prompting strategy.

---

# Sample Document

Artificial Intelligence (AI) is transforming industries by enabling machines to perform tasks that normally require human intelligence. AI applications include healthcare, finance, education, transportation, and cybersecurity.

Machine Learning (ML) is a subset of AI where algorithms learn patterns from data without being explicitly programmed. Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.

Natural Language Processing (NLP) allows computers to understand and generate human language. It powers chatbots, translators, virtual assistants, and text summarization systems.

Computer Vision enables machines to interpret images and videos. Examples include face recognition, medical image analysis, and autonomous vehicles.

Prompt Engineering is the practice of designing instructions that help AI models generate accurate and useful responses. Good prompts include clear instructions, relevant context, and specific objectives.

Large Language Models (LLMs) such as GPT can perform reasoning, coding, summarization, translation, and many other tasks.

The quality of an AI response depends on the clarity of the prompt, the relevance of the provided context, and the model's capabilities.

---

# Strategy 1 – Dump Everything

## Prompt

```
Read the following document carefully.

[Paste the complete document.]

Question:
What is Prompt Engineering?
```

### Output

Prompt Engineering is the practice of designing instructions that help AI models generate accurate and useful responses.

**Approximate Token Count**

- Prompt: 170
- Response: 18
- Total: 188

## Screenshots
<img width="1265" height="744" alt="image" src="https://github.com/user-attachments/assets/dd0b71fb-ae72-471f-af78-00f4ce98b063" />

---

# Strategy 2 – Question at the End

## Prompt

```
You are an AI assistant.

<context>

Paste the complete document here.

</context>

Answer only using the context above.

Question:
What is Prompt Engineering?
```

This strategy places the question after the context, following the guide's recommendation to reduce the "lost in the middle" effect.

### Output

Prompt Engineering is the practice of designing instructions that help AI models generate accurate and useful responses.

**Approximate Token Count**

- Prompt: 175
- Response: 18
- Total: 193

## Screenshots
<img width="1296" height="729" alt="image" src="https://github.com/user-attachments/assets/34f45953-716e-4a89-b93d-e14ab166512a" />

---

# Strategy 3 – Trimmed Context

## Prompt

```
Context:

Prompt Engineering is the practice of designing instructions that help AI models generate accurate and useful responses.

Question:
What is Prompt Engineering?
```

### Output

Prompt Engineering is the practice of designing instructions that help AI models generate accurate and useful responses.

**Approximate Token Count**

- Prompt: 40
- Response: 18
- Total: 58

## Screenshots
<img width="1151" height="676" alt="image" src="https://github.com/user-attachments/assets/e5910c2f-e36c-4eaf-a560-c00c20f37a7c" />

---

# Comparison

| Strategy | Accuracy | Approximate Tokens |
|----------|----------|-------------------:|
| Dump Everything | High | 188 |
| Question at the End | High | 193 |
| Trimmed Context | High | 58 |

---

# Conclusion

Three different context engineering strategies were tested.

- **Strategy 1** produced the correct answer but included unnecessary information, resulting in higher token usage.
- **Strategy 2** improved prompt organization by placing the question after the document, making it easier for the model to focus on the task.
- **Strategy 3** produced the same accurate answer while using the fewest tokens because only the relevant context was provided.

## Best Strategy

**Strategy 3 – Trimmed Context**

### Reason

Providing only the relevant context is the most efficient approach because it minimizes token usage while maintaining answer quality. This aligns with the guide's principle of treating the context window as a limited budget and avoiding unnecessary information.

---

# Learning Outcome

Through this exercise, I learned that effective context engineering is not about providing more information but about providing the **right information**. Well-organized and concise prompts improve response quality, reduce token consumption, and make AI systems more efficient.
