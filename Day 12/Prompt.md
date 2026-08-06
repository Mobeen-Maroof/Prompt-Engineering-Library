# Day 12 – Structured Outputs Your Code Can Trust

## Objective

The objective of this exercise is to generate structured JSON outputs from an AI model, validate them using a **Pydantic schema**, and automatically retry when invalid or incomplete data is returned. This ensures that AI responses are reliable and can be safely used in software applications.

---

# Introduction

When AI responses are used inside real applications, returning plain text is often not enough. Developers need responses in a predictable structure such as JSON.

In this activity, a Pydantic model was created to define the expected output format. Every AI response was validated against this schema. If validation failed because of missing fields or incorrect data types, the system automatically retried before reporting an error.

---

# Technologies Used

- Python 3
- Pydantic
- JSON
- ChatGPT
- GitHub

---

# Pydantic Schema

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category: str
    price: float
    in_stock: bool
```
---
## AI Response
<img width="1411" height="951" alt="image" src="https://github.com/user-attachments/assets/6daf873c-1b06-4063-be9c-1809557a78b1" />

---
# AI Prompt

```
Extract the product information below.

Return ONLY valid JSON.

Use exactly these keys:

name (string)

category (string)

price (number)

in_stock (boolean)

<document>

Laptop

Electronics

Price: $850.50

Available

</document>
```
---

# AI Response
<img width="1373" height="757" alt="image" src="https://github.com/user-attachments/assets/bbfadf16-863b-487c-baf8-482e370c463c" />

---

# Prompt with Missing Field

```
Extract the product information below.

Return ONLY valid JSON.

Use exactly these keys:

name

category

price

in_stock

<document>

Bottle

Kitchen

Available

</document>
```

---

# AI Response
<img width="1197" height="718" alt="image" src="https://github.com/user-attachments/assets/671eef74-d34b-484b-b8b6-38524f0ba462" />

---

# Prompt with Invalid Price

```
Extract the product information below.

Return ONLY valid JSON.

<document>

Chair

Furniture

Price: ABC

Available

</document>
```

---

# AI Response

<img width="1192" height="698" alt="image" src="https://github.com/user-attachments/assets/0594312c-9e59-4e17-8a07-daa39e37f399" />

---

# Prompt 4

```
Extract the product information below.

Return ONLY valid JSON.

<document>

Notebook

Stationery

Price: 5.99

Available

</document>
```

---

# AI Response
<img width="1261" height="728" alt="image" src="https://github.com/user-attachments/assets/936b48ce-6bcd-4bfa-bae8-cca0053571d1" />

---

# Prompt 5

```
Extract the product information below.

Return ONLY valid JSON.

<document>

Headphones

Electronics

Price: 49.99

Not Available

</document>
```

---

# AI Response
<img width="1165" height="698" alt="image" src="https://github.com/user-attachments/assets/c7220ef2-0a5f-4796-a132-a6f65f6ee651" />

---

# Test Results

| Test | Input | Validation Result |
|------|-------|-------------------|
| Test 1 | Laptop | ✅ Passed |
| Test 2 | Notebook | ✅ Passed |
| Test 3 | Headphones | ✅ Passed |
| Test 4 | Chair (Invalid Price) | ❌ Failed |
| Test 5 | Bottle (Missing Price) | ❌ Failed |

---

# Validation and Retry

The Python program validated every JSON response using the Pydantic schema.

If a required field was missing or a data type was incorrect, the validation failed. The system automatically retried before reporting the error.

---

# Observation

Using structured JSON together with Pydantic validation makes AI outputs more reliable. Instead of accepting any text, the application checks whether the response follows the required schema. This reduces errors and prevents invalid data from entering the system.

---

# Conclusion

This exercise demonstrated how structured outputs improve the reliability of AI-powered applications. By combining JSON formatting, Pydantic validation, retry logic, and clear document delimiters, developers can safely integrate AI responses into real-world software systems.

---

# Skills Learned

- Structured Output Generation
- JSON Formatting
- Pydantic Schema Validation
- Automatic Retry Logic
- Prompt Engineering
- Data Validation
- Python Programming
- AI Integration

---
