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
