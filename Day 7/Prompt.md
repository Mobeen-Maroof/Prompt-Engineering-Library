# Day 7 – Prompt Pattern Library

## Objective

Build a reusable Prompt Pattern Library containing five prompt templates that demonstrate the techniques learned throughout Week 1.

---

# Template 1 – Summarize

## Template

Summarize the following text for {target_audience}.

Requirements:

- Maximum {word_limit} words.
- Highlight the most important points.
- Use clear and simple language.

Text:

Artificial Intelligence helps computers perform tasks that normally require human intelligence, such as recognizing images, understanding language, and making predictions. AI is widely used in healthcare, education, finance, and transportation.

---

## Why

This template uses specificity by defining the audience and word limit. These constraints help the AI generate summaries that match the user's needs without unnecessary details.

---

## A/B Comparison

### Naive Prompt

Summarize this text.

### Screenshot of response
<img width="1211" height="588" alt="image" src="https://github.com/user-attachments/assets/fb6db955-59c6-4977-8968-44135df61ee8" />

### Improved Prompt

Summarize the following article for first-year Computer Science students.

Requirements:
- Maximum 120 words.
- Highlight the three most important ideas.
- Use simple language.

### Screenshot of response
<img width="1205" height="777" alt="image" src="https://github.com/user-attachments/assets/b6ed59f9-becb-414b-ae0d-9b990e55a9f0" />

### Result

The improved prompt produced a concise summary tailored to the intended audience.

---

# Template 2 – Extract

## Template

Extract the following fields from the text into a valid JSON object.

Fields:

{field_list}

Rules:

- Output ONLY valid JSON.
- If a field is missing, use null.
- Do not guess.
- Begin your response with {

Text:

John Smith

Email:
john@gmail.com

Phone:
+92 300 1234567

---

## Why

This template combines positive instructions, format control, and the null rule to generate reliable JSON that can be parsed directly by software.

---

## A/B Comparison

### Naive Prompt

Extract the information as JSON.

### Screenshot of response
<img width="1232" height="799" alt="image" src="https://github.com/user-attachments/assets/7ef63eb2-812a-453e-9e0e-1fd49071e53e" />

### Improved Prompt

Extract the following information into valid JSON.

Fields:

{
"name":"",
"email":"",
"phone":""
}

Rules:

Output ONLY JSON.

Use null if any field is missing.

### Screenshot of response
<img width="1242" height="662" alt="image" src="https://github.com/user-attachments/assets/1e2a69a2-59ec-40f9-822b-4bf5ac9731af" />

### Result

The improved prompt produced clean, parseable JSON without extra explanations.

---

# Template 3 – Classify

## Template

Classify each item into one of these categories:

{category_list}

Examples:

{few_shot_examples}

Items:

{input_text}

Return only the item and its category.

---

## Why

This template uses few-shot prompting to teach the model the expected classification pattern, improving consistency.

---

## A/B Comparison

### Naive Prompt

Classify these messages.

### Screenshot of response
<img width="1151" height="557" alt="image" src="https://github.com/user-attachments/assets/31672ac6-d7a4-4781-a7fb-3ee4de1b8f49" />

### Improved Prompt

Classify these customer support messages.

Categories:

Bug

Question

Praise

Complaint

Example:

"The app crashes." → Bug

Messages:

1. Excellent service!

2. How do I reset my password?

3. The website is slow.

Return only the message number and category.

### Screenshot of response
<img width="1116" height="706" alt="image" src="https://github.com/user-attachments/assets/49a83e63-bc53-4eab-b31d-e5198e220d2b" />

### Result

The improved prompt produced more consistent and accurate classifications.

---

# Template 4 – Rewrite

## Template

Rewrite the following text.

Audience:

{target_audience}

Tone:

{tone}

Requirements:

- Keep the original meaning.
- Improve clarity.
- Correct grammar.
- Do not add new information.

Text:

I like AI because it helps me learn faster and make better projects.

---

## Why

This template combines audience specification and tone control while preserving the original meaning, making rewritten content more appropriate for its intended readers.

---

## A/B Comparison

### Naive Prompt

Rewrite this paragraph.

### Screenshot of response
<img width="1160" height="777" alt="image" src="https://github.com/user-attachments/assets/8975fc34-00f0-4e1a-8923-ff1773a2857d" />

### Improved Prompt

Rewrite the following paragraph for a professional audience.

Tone:

Formal

Requirements:

- Keep the meaning the same.
- Improve grammar.
- Improve clarity.

Paragraph:

I like AI because it helps me learn faster and make better projects.

### Screenshot of response
<img width="1276" height="757" alt="image" src="https://github.com/user-attachments/assets/6e12bbc6-bd85-4a76-ba55-d0551a3f2e56" />

### Result

The improved prompt generated a polished version that matched the target audience.

---

# Template 5 – Question Answering on a Source

## Template

Using ONLY the document below, answer the question.

If the answer is not clearly stated, reply:

"Not stated in the document."

Document:

{source_text}

Question:

What salary do TechNova interns receive?

---

## Why

This template reduces hallucinations by grounding the AI in the provided document and allowing it to admit when information is unavailable.

---

## A/B Comparison

### Naive Prompt

Answer this question.

### Screenshot of response
<img width="1255" height="513" alt="image" src="https://github.com/user-attachments/assets/b7042069-5ea2-4469-ac13-75cc8b3baece" />

### Improved Prompt

Using ONLY the document below, answer the question.

If the answer is not clearly mentioned, reply:

Not stated in the document.

Document:

TechNova Solutions is hiring Software Engineer Interns.

Applications close on August 15, 2026.

Question:

What salary will interns receive?

### Screenshot of response
<img width="1257" height="692" alt="image" src="https://github.com/user-attachments/assets/69c3a484-8062-4aa5-8566-d85332290a97" />

### Result

The improved prompt avoided unsupported claims and produced more reliable answers.

---

# Reflection

This week taught me that effective prompt engineering is about giving clear instructions, providing enough context, and defining the desired output. I learned that techniques such as roles, few-shot prompting, format control, and grounding significantly improve AI responses. Building this Prompt Pattern Library has given me reusable templates that I can apply in future AI and machine learning projects.
