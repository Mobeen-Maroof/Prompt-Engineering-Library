# Day 16 – RAG Prompting (Retrieval-Augmented Generation)

## Overview

This exercise demonstrates **Retrieval-Augmented Generation (RAG)**, a technique that improves the reliability of AI responses by retrieving relevant information from external documents before generating an answer. Instead of relying on the model's memory, the AI is instructed to answer **only from the provided sources**, include citations, and refuse to answer if the information is unavailable.

---

# Objective

- Understand the concept of Retrieval-Augmented Generation (RAG).
- Create a small knowledge base.
- Write a grounding prompt with citations.
- Test answerable, partially answerable, and unanswerable questions.
- Ensure the model refuses questions outside the provided sources.

---

# Knowledge Base (Documents)

## Document 1

Artificial Intelligence (AI) is the simulation of human intelligence by machines. AI systems can perform tasks such as learning, reasoning, problem-solving, and decision-making.

---

## Document 2

Machine Learning (ML) is a subset of Artificial Intelligence. Instead of following explicit programming instructions, ML algorithms learn patterns from training data to make predictions or decisions.

---

## Document 3

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple hidden layers. It is commonly used in image recognition, speech recognition, and natural language processing.

---

## Document 4

Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. Common NLP applications include chatbots, translators, sentiment analysis, and text summarization.

---

## Document 5

Prompt Engineering is the practice of designing effective prompts that guide Large Language Models to generate accurate, relevant, and reliable responses.

---

## Document 6

Large Language Models (LLMs) are AI models trained on massive amounts of text data. They can perform tasks such as question answering, summarization, translation, coding, and reasoning.

---

## Document 7

Computer Vision allows computers to analyze and understand images and videos. It is widely used in facial recognition, autonomous vehicles, and medical imaging.

---

## Document 8

Retrieval-Augmented Generation (RAG) combines information retrieval with language generation. Relevant documents are retrieved first, and the language model generates answers using only those retrieved documents.

---

## Document 9

Embedding models convert text into numerical vectors that capture semantic meaning. These vectors help retrieve relevant documents during similarity search.

---

## Document 10

FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and vector retrieval. It is commonly used to build RAG systems.

---

# Grounding Prompt

```
You are an AI assistant.

Answer the question using ONLY the provided sources.

Rules:

1. Do not use outside knowledge.
2. Cite the document number after every answer.
3. If the answer is not available in the documents, respond exactly with:

"I couldn't find that in the provided sources."

Sources:

[1] Artificial Intelligence...
[2] Machine Learning...
...
[10] FAISS...

Question:
{User Question}
```

This prompt enforces grounding, citations, and a clear refusal when the answer is not present, which are the key ideas emphasized in the guide. :contentReference[oaicite:1]{index=1}

---

# Test Questions and Results

## Question 1

**What is Machine Learning?**

### Answer

Machine Learning is a subset of Artificial Intelligence that enables algorithms to learn patterns from training data instead of relying on explicit programming. **[Document 2]**

### Screenshots
<img width="1134" height="669" alt="image" src="https://github.com/user-attachments/assets/840224d9-0bcb-43d9-b2f3-7846af715025" />

---

## Question 2

**What is FAISS used for?**

### Answer

FAISS is used for efficient similarity search and vector retrieval in Retrieval-Augmented Generation (RAG) systems. **[Document 10]**

### Screenshots
<img width="1143" height="187" alt="image" src="https://github.com/user-attachments/assets/e16e90ee-88d8-4609-a69a-0640003b5963" />

---

## Question 3

**Explain Retrieval-Augmented Generation (RAG).**

### Answer

Retrieval-Augmented Generation (RAG) combines document retrieval with language generation. Relevant documents are retrieved first, and the language model generates responses using only those retrieved documents. **[Document 8]**

### Screenshots
<img width="1121" height="172" alt="image" src="https://github.com/user-attachments/assets/e1d9e4a6-af5b-476b-af74-c6d98543f0e4" />

---
## Question 4

**What is Prompt Engineering?**

### Answer

Prompt Engineering is the practice of designing effective prompts that guide Large Language Models to generate accurate, relevant, and reliable responses.

### Screenshots
<img width="1075" height="131" alt="image" src="https://github.com/user-attachments/assets/165ce2a8-fe76-47a7-b254-9ed859612ecb" />

---

## Question 5

**Who invented Python?**

### Answer

**I couldn't find that in the provided sources.**

### Screenshots
<img width="901" height="87" alt="image" src="https://github.com/user-attachments/assets/0c21bf18-9eff-4709-a189-ee3ece39fbea" />

---

# Faithfulness Test

## Unfaithful Response

Question:

Who invented Python?

Wrong Answer:

Python was invented by Guido van Rossum.

### Screenshots
<img width="1111" height="274" alt="image" src="https://github.com/user-attachments/assets/db0f22ca-958a-4829-b729-23f4514d7165" />

Problem:

Although the answer is factually correct, it does not exist in the provided documents. Therefore, the model used outside knowledge, making the response unfaithful.

---

## Faithful Response

Question:

Who invented Python?

Answer:

I couldn't find that in the provided sources.

### Screenshots
<img width="871" height="105" alt="image" src="https://github.com/user-attachments/assets/6d7db850-4fee-485e-8261-d1ac325e9ba6" />

Reason:

The information is not available in the knowledge base, so the model correctly refused to answer.

---

# Comparison

| Question | Retrieved from Documents | Citation | Faithful |
|-----------|-------------------------|----------|-----------|
| Machine Learning | Yes | Document 2 | ✅ |
| Prompt Engineering | Yes | Document 5 | ✅ |
| FAISS | Yes | Document 10 | ✅ |
| RAG | Yes | Document 8 | ✅ |
| Python Inventor | No | None | ✅ Refused |

---

# Conclusion

This exercise demonstrates how Retrieval-Augmented Generation (RAG) improves the reliability of AI-generated responses by grounding answers in retrieved documents. Using a grounding prompt with citations ensures transparency, while the refusal mechanism prevents the model from generating unsupported information. The experiment highlights that trustworthy AI systems depend on both accurate retrieval and strict adherence to the provided sources. :contentReference[oaicite:2]{index=2}

---

# Learning Outcome

Through this exercise, I learned that Retrieval-Augmented Generation (RAG) makes AI systems more reliable by combining document retrieval with response generation. By limiting answers to retrieved sources, adding citations, and refusing unsupported questions, AI systems become more transparent, accurate, and trustworthy.
