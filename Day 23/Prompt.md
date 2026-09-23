# Day 23 – Promptfoo Evaluation

## 📌 Overview

The **Promptfoo Evaluation** project demonstrates how to evaluate and compare multiple prompts using the Promptfoo evaluation framework.

In this project, I reused the **20 sentiment classification test cases from Day 22** and evaluated two different prompt versions using a local **Ollama Llama 3.2** model.

Promptfoo automatically executed the test cases, compared the model outputs with the expected answers, and generated a prompt comparison matrix.

---

## 🎯 Objective

The objective of this project is to learn how to use Promptfoo for systematic prompt evaluation and testing.

The project demonstrates:

- Prompt evaluation using Promptfoo
- Comparison of multiple prompt variants
- Reusing a fixed evaluation dataset
- Automated pass/fail testing
- Local LLM evaluation with Ollama
- Prompt performance comparison

---

## ✨ Features

- 🧪 20 sentiment classification test cases
- 🔄 Two prompt variants
- 🤖 Ollama Llama 3.2 integration
- ⚙️ Automated Promptfoo evaluation
- 📊 Pass/Fail comparison
- 📝 Expected vs predicted output validation
- 💻 Local LLM evaluation
- 📈 Prompt comparison matrix

---

 ## Technologies Used
- Promptfoo
- Node.js
- npm
- Ollama
- Llama 3.2
- YAML
- Prompt Engineering
- Automated Evaluation
- Git & GitHub

---

## Test Dataset

The project uses the same 20 sentiment classification cases created during Day 22.

Each test case contains:

- Input text
- Expected sentiment label

The available sentiment labels are:

- Positive
- Negative
- Mixed

Example:
- vars:
    text: "The delivery was quick, but the product quality was terrible."
  assert:
    - type: equals
      value: "Mixed"

---

## 📝 Prompt Variants

Two different prompt versions were evaluated.

### Prompt 1 – Baseline Prompt

The first prompt provides basic instructions for classifying text as:

Positive
Negative
Mixed

It also instructs the model to return only one label.

### Prompt 2 – Strict Classification Prompt

The second prompt provides more detailed classification rules and instructs the model to:

Read the complete input.
Select exactly one label.
Consider the overall opinion.
Return only the classification.
Avoid explanations.

---

## 🤖 Model Provider

The evaluation uses the local Ollama model:

ollama:chat:llama3.2

This allows the evaluation to run locally without requiring an OpenAI API key.

---

## 📊 Promptfoo Evaluation

The evaluation was executed using:

npx promptfoo@latest eval

Promptfoo evaluated:

20 test cases × 2 prompts = 40 evaluations

---

## 📈 Evaluation Results

The actual Promptfoo evaluation produced:

Total Evaluations : 40
Passed            : 33
Failed            : 7
Errors            : 0
Overall Pass Rate : 82.50%

---

### Results Summary
Metric	Result
Test Cases	20
Prompt Variants	2
Total Evaluations	40
Passed	33
Failed	7
Errors	0
Overall Pass Rate	82.50%

---

### 🔍 Example Evaluation Results
#### Example 1
Input:
The product is absolutely fantastic and works perfectly.

Prompt 1:
PASS → Positive

Prompt 2:
PASS → Positive

#### Example 2
Input:
The price is reasonable and the quality is excellent.

Expected:
Positive

Prompt 1:
FAIL → Mixed

Prompt 2:
PASS → Positive

#### Example 3
Input:
The product is expensive, unreliable, and disappointing.

Expected:
Negative

Prompt 1:
FAIL → Mixed

Prompt 2:
PASS → Negative

#### Example 4
Input:
The quality is better than I expected.

Expected:
Positive

Prompt 1:
FAIL → Mixed

Prompt 2:
PASS → Positive

These examples demonstrate how Promptfoo identifies differences between prompt variants using the same test cases.

---
## Screenshots of Output

<img width="1363" height="884" alt="image" src="https://github.com/user-attachments/assets/3916554c-2eb1-4e85-9bd9-50fb4cf693ba" />
<img width="1322" height="831" alt="image" src="https://github.com/user-attachments/assets/b44c84e7-87e1-4207-9ea2-899f10fdc7d7" />
<img width="1320" height="854" alt="image" src="https://github.com/user-attachments/assets/d1a3ae5d-c82e-42c1-9a67-60405be05b3c" />
<img width="1305" height="778" alt="image" src="https://github.com/user-attachments/assets/cf46ce39-354b-42a4-80b4-72466e7b3ca4" />

---

## Screenshot of browser
<img width="1911" height="914" alt="image" src="https://github.com/user-attachments/assets/1c75adf3-b8c5-4f78-999b-22accb797907" />
<img width="1896" height="814" alt="image" src="https://github.com/user-attachments/assets/fe851cb5-537a-4a7b-82c2-a12a91fb16d6" />
<img width="1919" height="888" alt="image" src="https://github.com/user-attachments/assets/4c0950d5-8949-4d1c-97d8-2b9a6c2b96b6" />
<img width="1896" height="868" alt="image" src="https://github.com/user-attachments/assets/eb6b3a9f-ec88-46f1-809b-7ed6334ba6ae" />
<img width="1909" height="864" alt="image" src="https://github.com/user-attachments/assets/19a6d5c9-cd7f-4a87-8e0d-d3e8ec09f308" />
<img width="1871" height="812" alt="image" src="https://github.com/user-attachments/assets/9cad640e-b653-4f5f-8f4d-a599123f1cba" />
<img width="1883" height="751" alt="image" src="https://github.com/user-attachments/assets/d163515a-6f1b-4b5b-9082-a9af5e719a22" />
<img width="1911" height="791" alt="image" src="https://github.com/user-attachments/assets/13783280-dad7-4a7c-aaaa-64ea37bebc41" />
<img width="1899" height="866" alt="image" src="https://github.com/user-attachments/assets/4db93681-dccb-4d60-8de2-bf763649169d" />
<img width="1869" height="829" alt="image" src="https://github.com/user-attachments/assets/42017bae-23b1-4adf-b315-556f262c6ac9" />
<img width="1908" height="811" alt="image" src="https://github.com/user-attachments/assets/21918e9e-f017-4d02-8caf-cf09ab66a839" />

### Prompt
<img width="1853" height="829" alt="image" src="https://github.com/user-attachments/assets/12564925-fa10-4b5c-94d3-a1da3b3b0667" />
<img width="1742" height="785" alt="image" src="https://github.com/user-attachments/assets/bbb7603e-8cf0-4779-a2e3-70c40d18de6a" />
<img width="1721" height="800" alt="image" src="https://github.com/user-attachments/assets/8fbe5793-aab5-45b7-91ac-a393408cfbbc" />

### Datasets
<img width="1880" height="726" alt="image" src="https://github.com/user-attachments/assets/1dd51e05-7ae3-45f4-9246-ee59a199986d" />
### History

<img width="1880" height="892" alt="image" src="https://github.com/user-attachments/assets/b642c223-a4b6-474c-8a3f-ccc44c56697d" />

---

## 🔄 Evaluation Workflow
Day 22 Test Dataset
        │
        ▼
Two Prompt Variants
        │
        ▼
Promptfoo Configuration
        │
        ▼
Ollama Llama 3.2
        │
        ▼
Run 20 Test Cases
        │
        ▼
40 Total Evaluations
        │
        ▼
PASS / FAIL Results
        │
        ▼
Prompt Comparison

---
## 📚 Learning Outcomes

Through this project, I learned how to:

- Use Promptfoo for prompt evaluation.
- Create a Promptfoo configuration file.
- Compare multiple prompt variants.
- Reuse a fixed test dataset.
- Evaluate prompts automatically.
- Connect Promptfoo with a local Ollama model.
- Analyze PASS and FAIL results.
- Compare prompt behavior using consistent test cases.
- Understand the importance of automated prompt testing.

---

## 🔮 Future Improvements
- Add larger test datasets.
- Add more prompt variants.
- Add additional evaluation metrics.
- Test different LLM models.
- Add custom evaluation criteria.
- Automate evaluation reports.
- Add regression testing for future prompt changes.
- Integrate Promptfoo evaluation into CI/CD workflows.

---

## 🎓 Key Concepts
- Prompt Evaluation
- Prompt Testing
- Promptfoo
- Prompt Comparison
- Test-Driven Prompt Engineering
- Automated Evaluation
- LLM Evaluation
- Ollama
- Llama 3.2
- Regression Testing
- YAML Configuration

---

## 👨‍💻 Author

**Mobeen Maroof**

GitHub Learning Journey – Prompt Engineering & AI Agents
