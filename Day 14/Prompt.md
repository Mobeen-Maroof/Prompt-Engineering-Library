# Day 14 – Structured Extraction Pipeline

## Objective

This project demonstrates a complete structured extraction pipeline that converts unstructured product information into validated JSON records. The pipeline includes extraction, self-critique, correction, and schema validation using Pydantic.

---

# Pipeline Stages

### Stage 1 – Extract

Extract product information from unstructured text and convert it into JSON.

### Stage 2 – Self Critique

Review the extracted JSON for missing fields and invalid values.

### Stage 3 – Correct

Automatically fix missing or invalid fields before validation.

### Stage 4 – Validate

Validate the corrected JSON using a Pydantic schema.

---

# Technologies Used

- Python
- Pydantic
- JSON
- ChatGPT
- GitHub

---

# Pydantic Schema

```python
class Product(BaseModel):
    name: str
    category: str
    price: float
    in_stock: bool
```
---
## Output Screenshot
<img width="1256" height="902" alt="image" src="https://github.com/user-attachments/assets/ad6252cc-d0cf-4af3-a625-d296d50f3946" />

---
# Single Prompt
```
Extract the following product into valid JSON.

Return ONLY JSON.

Schema:

name

category

price

in_stock

<document>

Product: Laptop

Category: Electronics

Price: 850.50

Available: Yes

</document>
```
---
## AI Response
<img width="1209" height="719" alt="image" src="https://github.com/user-attachments/assets/2e7ab87f-5b57-4d5d-a8dc-20bb0d0ab9f5" />

---
## Self Critique Prompt
```
Review this JSON.

Check:

- Missing fields

- Incorrect values

- Invalid data types

Return corrections only.

{
"name":"Chair",
"category":"Furniture",
"price":"ABC",
"in_stock":true
}
```
---
## AI Response
<img width="1219" height="749" alt="image" src="https://github.com/user-attachments/assets/ee69ce31-8737-44b8-a31e-e1c365b3dfb9" />

---
## Correct Prompt
```
Correct this JSON.

{
"name":"Chair",
"category":"Furniture",
"price":"ABC",
"in_stock":true
}
```
---
## AI Response
<img width="1236" height="698" alt="image" src="https://github.com/user-attachments/assets/338ae7fb-40c6-4c34-a1af-0d7dcbfef30b" />

---
# Test Results

| Document | Result |
|-----------|--------|
| Laptop | ✅ Passed |
| Notebook | ✅ Passed |
| Headphones | ✅ Passed |
| Chair | ✅ Corrected |
| Bottle | ✅ Corrected |
| Mouse | ✅ Passed |
| Keyboard | ✅ Passed |

---

# Reflection

The pipeline successfully handled valid records and automatically corrected missing or invalid values before validation. The self-critique stage helped identify errors, making the overall extraction process more reliable. Future improvements could include extracting data directly from PDFs or emails and supporting more complex document formats.

---

# Repository Structure

```
Day14/

│

├── extraction_pipeline.py

├── test_documents.txt

```

---
