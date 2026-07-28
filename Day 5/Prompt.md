# Day 5 – Controlling the Output Format

## Objective

Learn how to control AI output formats by generating valid JSON, Markdown tables, and plain prose.

---

# Source Text

Software Engineer Internship

Company: TechNova Solutions

Location: Karachi, Pakistan

Salary: PKR 50,000/month

Requirements:
- Python
- Machine Learning
- Git
- Communication Skills

Apply before August 15, 2026

Email:
careers@technova.com

---

# Prompt 1 – JSON Extraction

Extract the following information from the job advertisement into a single valid JSON object.

Fields:

{
  "job_title": string,
  "company": string,
  "location": string,
  "salary": string,
  "skills": array,
  "deadline": string,
  "email": string
}

Rules:

- Output ONLY the JSON object.
- Do not include explanations.
- If any field is missing, use null.
- Begin your response with {

Job Advertisement:

Software Engineer Internship

Company: TechNova Solutions

Location: Karachi, Pakistan

Salary: PKR 50,000/month

Requirements:
Python
Machine Learning
Git
Communication Skills

Apply before August 15, 2026

Email:
careers@technova.com

## AI Response
<img width="1059" height="803" alt="image" src="https://github.com/user-attachments/assets/f3da95c2-a9bd-4443-8804-4381927b14b3" />

---

# Prompt 2 – Markdown Table

Convert the following job advertisement into a Markdown table.

Job Advertisement:

Software Engineer Internship

Company: TechNova Solutions

Location: Karachi, Pakistan

Salary: PKR 50,000/month

Requirements:
Python
Machine Learning
Git
Communication Skills

Apply before August 15, 2026

Email:
careers@technova.com

## AI Response
<img width="1200" height="738" alt="image" src="https://github.com/user-attachments/assets/c98f4816-c482-42ab-b3b5-c6138374de3d" />

---

# Prompt 3 – Plain Prose

Rewrite the following job advertisement as one professional paragraph.

Software Engineer Internship

Company: TechNova Solutions

Location: Karachi, Pakistan

Salary: PKR 50,000/month

Requirements:
Python
Machine Learning
Git
Communication Skills

Apply before August 15, 2026

Email:
careers@technova.com

## AI Response
<img width="1267" height="741" alt="image" src="https://github.com/user-attachments/assets/181f309e-8d8a-40b0-bb9d-3bec90dc6897" />

---

# Python Validation
<img width="1777" height="922" alt="image" src="https://github.com/user-attachments/assets/7277165f-ffd3-4843-9818-776557e0c69f" />

The JSON output was successfully validated using Python's `json.loads()` function.

---

# Conclusion

This exercise showed how prompt wording controls output format. Using positive instructions, requiring only JSON, adding a `null` rule, and beginning with `{` helped produce structured output that could be parsed successfully in Python. The same information was also represented as a Markdown table and a paragraph, demonstrating flexible format control.
