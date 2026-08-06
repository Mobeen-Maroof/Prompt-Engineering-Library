# Day 13 – Meta Prompting: Use the Model to Write Better Prompts

## Objective

The objective of this exercise is to learn how to improve prompts using AI itself. Instead of writing better prompts manually, we use a reusable prompt-improver that transforms simple prompts into more detailed, reusable, and reliable versions.

---

# Introduction

Meta-prompting means creating prompts that improve other prompts. Rather than focusing on solving a task directly, the model analyzes an existing prompt and rewrites it to make it clearer, more specific, and easier to reuse.

This technique helps developers build high-quality prompt libraries for future AI applications.

---

# Prompt Improver

## Prompt

```text
You are an expert Prompt Engineer.

Improve the prompt below.

Requirements:

- Keep the same goal.
- Make it more specific.
- Add clear instructions.
- Improve reliability.
- Use placeholders where appropriate.

Return:

1. Improved Prompt

2. Explain what changed and why.

Prompt:

"""
{prompt}
"""
```

---

# Template 1

## Original

```
Explain Machine Learning.
```

## Improved Prompt Screenshot
<img width="989" height="797" alt="image" src="https://github.com/user-attachments/assets/e1d463e4-4e4f-4026-8282-c05942e511aa" />
<img width="1013" height="376" alt="image" src="https://github.com/user-attachments/assets/af6e7c4d-4fe2-4915-a41b-ce61ad69386f" />

## Improved Prompt Response
<img width="1139" height="734" alt="image" src="https://github.com/user-attachments/assets/4c17d6cb-acdb-4df0-afcf-58714c762c78" />
<img width="1030" height="760" alt="image" src="https://github.com/user-attachments/assets/3cf21070-d21a-4222-8751-31c043bb2485" />
<img width="1120" height="689" alt="image" src="https://github.com/user-attachments/assets/330dc6b6-83cb-4cc6-8325-529a3bf938c6" />

### Verdict
The improved prompt is better because it clearly defines the audience, required sections, and response length.

---

# Template 2

## Original

```
Summarize this article.
```

## Improved Prompt Screenshot
<img width="1034" height="734" alt="image" src="https://github.com/user-attachments/assets/acfda6ce-9dfc-4ac6-9f82-d69a26ba8253" />
<img width="1118" height="361" alt="image" src="https://github.com/user-attachments/assets/16df826f-a0a7-4902-8e8f-78531346ebda" />

## Improved Prompt Response
<img width="1248" height="698" alt="image" src="https://github.com/user-attachments/assets/dd78cfd1-8a86-4d82-863b-75eec76b0fc0" />

### Verdict

The improved prompt is reusable and allows different audiences and article lengths by using placeholders.

---

# Template 3

## Original

```
Write Bubble Sort code.
```

## Improved Prompt Screenshot
<img width="1069" height="731" alt="image" src="https://github.com/user-attachments/assets/2416b361-7892-4765-871a-9a1909089da1" />
<img width="1067" height="291" alt="image" src="https://github.com/user-attachments/assets/f4926b66-4a66-452d-87ff-6106c4b83aee" />

## Improved Prompt Response
<img width="1105" height="773" alt="image" src="https://github.com/user-attachments/assets/9f53ec11-5c18-4424-ba28-28115c3c57a2" />
<img width="1042" height="790" alt="image" src="https://github.com/user-attachments/assets/debd95b4-b4d5-463c-b198-14f5f5f1fe05" />
<img width="1178" height="476" alt="image" src="https://github.com/user-attachments/assets/813416c8-854a-4013-8c02-03130ce11dc0" />
<img width="1220" height="761" alt="image" src="https://github.com/user-attachments/assets/8ce19c7c-c2db-48bb-8d29-796bfc801cde" />
<img width="1048" height="595" alt="image" src="https://github.com/user-attachments/assets/895272e0-29a7-405f-9081-6a6898edcb6f" />

### Verdict

The improved version provides clear expectations and generates more educational code.

---

# Parameterized Template

```text
Explain Data Science

Audience:

University Students

Maximum Words:

300 words

Include:

- Definition
- Key Concepts
- Example
- Applications

Output Format:

Markdown
```
---

## AI Response
<img width="1153" height="752" alt="image" src="https://github.com/user-attachments/assets/bf2e4bd0-6df3-4247-acfb-399d34e1a71e" />
<img width="1104" height="756" alt="image" src="https://github.com/user-attachments/assets/74327ba4-05d1-4956-beeb-b7ef5e07403f" />
<img width="999" height="394" alt="image" src="https://github.com/user-attachments/assets/fae46425-3e13-4552-ae61-870f283eeb59" />

---

# Observation

The improved prompts produced more structured, detailed, and reusable responses than the original prompts. Named placeholders also make the prompts easier to reuse in software applications.

---

# Conclusion

Meta-prompting is an effective Prompt Engineering technique that allows AI to improve prompts automatically. Reusable prompt templates increase consistency, reduce ambiguity, and make prompts easier to integrate into real-world AI systems.

---

# Skills Learned

- Meta Prompting
- Prompt Improvement
- Prompt Templates
- Parameterized Prompts
- Prompt Reusability
- Prompt Engineering
- AI Optimization

---
