# Day 22 – Prompt Evaluation & Testing

## 📌 Overview

The **Prompt Evaluation & Testing** project demonstrates how to systematically measure the performance of prompts using a fixed test dataset and an automated scoring system.

The project compares a **baseline prompt** with a deliberately modified prompt using the same 20 test cases. The evaluation calculates accuracy for both versions and identifies whether the prompt modification improves or reduces performance.

---

## 🎯 Objective

The objective of this project is to build a simple and measurable prompt evaluation workflow that demonstrates:

- Prompt Testing
- Test Dataset Creation
- Baseline Evaluation
- Accuracy Scoring
- Prompt Comparison
- Regression Detection

---

## ✨ Features

- 🧪 20-case evaluation test set
- 📊 Automated accuracy calculation
- 📝 Baseline prompt evaluation
- 🔄 Improved prompt evaluation
- 📈 Before-and-after comparison
- ⚠️ Prompt regression detection
- 🐍 Python-based evaluation pipeline
- 🤖 Ollama and Llama 3.2 integration
- 📁 Structured JSON test dataset

---

## ⚙️ Technologies Used

- Python
- Ollama
- Llama 3.2
- JSON
- Prompt Engineering
- Automated Evaluation
- Accuracy Scoring
- Git & GitHub

---

## 🛠️ Components

### 🧪 Test Dataset

The project contains **20 test cases**.

Each test case includes:

- Input text
- Expected classification

The classification categories are:

- Positive
- Negative
- Mixed

Example:

```json
{
    "input": "The delivery was quick, but the product quality was terrible.",
    "expected": "Mixed"
}
```

---

### 📝 Baseline Prompt

The first version of the prompt is used as the baseline.

The model classifies every test case and the program calculates the percentage of correct predictions.

The baseline accuracy obtained was:

```text
90.00%
```

---

### 🔄 Improved Prompt

A deliberate modification was made to the original prompt.

The same 20 test cases were then evaluated again using the modified prompt.

The improved prompt accuracy was:

```text
80.00%
```
---

## Screenshots of Output
<img width="867" height="808" alt="image" src="https://github.com/user-attachments/assets/4d542a27-eb98-4389-a3f5-3aec49f998e4" />
<img width="1069" height="858" alt="image" src="https://github.com/user-attachments/assets/a5786649-25f6-43ce-94d3-735cbf57c583" />
<img width="1018" height="880" alt="image" src="https://github.com/user-attachments/assets/c746aedb-3501-4f7d-8468-3a1eb55d67f1" />
<img width="1058" height="870" alt="image" src="https://github.com/user-attachments/assets/75ee4d56-d19e-45ee-bfb7-d64dd638dd88" />
<img width="1067" height="809" alt="image" src="https://github.com/user-attachments/assets/60c631a8-41f3-44e9-ac1e-d4a87b3c8918" />
<img width="1017" height="840" alt="image" src="https://github.com/user-attachments/assets/2d2b1cfa-e480-4141-affe-c619a6beea73" />
<img width="1011" height="821" alt="image" src="https://github.com/user-attachments/assets/9a154b50-0d3b-4be7-ae01-2d77df141424" />
<img width="936" height="507" alt="image" src="https://github.com/user-attachments/assets/469bceaf-b718-4782-baf5-ac8aa2c035ea" />

---

### 📊 Evaluation & Scoring

The project uses accuracy to measure prompt performance.

The accuracy formula is:

```text
Accuracy = (Correct Predictions / Total Test Cases) × 100
```

The same test set is used for both prompt versions to make the comparison consistent.

---

## 📈 Evaluation Results

<img width="885" height="232" alt="image" src="https://github.com/user-attachments/assets/84cfde9d-fd75-4659-ab91-6570f0d25adf" />

### Results Table

| Metric | Result |
|---|---:|
| Total Test Cases | 20 |
| Baseline Accuracy | 90.00% |
| Improved Accuracy | 80.00% |
| Change | -10.00% |

---

## 🔍 Result Analysis

The baseline prompt achieved an accuracy of **90.00%**, while the modified prompt achieved **80.00%**.

The prompt modification resulted in a **10 percentage point decrease** in accuracy on this test set.

This demonstrates why prompt changes should be evaluated using a consistent test dataset instead of assuming that a modified prompt will automatically perform better.

The evaluation process successfully detected a **prompt regression**.

---

## 🔄 Evaluation Workflow

```text
Test Dataset
      │
      ▼
Baseline Prompt
      │
      ▼
Run 20 Test Cases
      │
      ▼
Calculate Accuracy
      │
      ▼
Modify Prompt
      │
      ▼
Run Same 20 Test Cases
      │
      ▼
Calculate Accuracy
      │
      ▼
Compare Results
```
---

## 🚀 Installation

### 1. Install Ollama

Install Ollama on your computer.

### 2. Pull the Model

```bash
ollama pull llama3.2
```

### 3. Install Python Dependency

```bash
pip install ollama
```

### 4. Run the Evaluation

```bash
py main.py
```

---

## 🧪 Evaluation Process

The program automatically:

1. Loads the test cases from `test_cases.json`.
2. Sends each input to the baseline prompt.
3. Records the model prediction.
4. Compares the prediction with the expected answer.
5. Calculates baseline accuracy.
6. Runs the same test cases with the modified prompt.
7. Calculates improved-prompt accuracy.
8. Displays the final comparison.

---

## 📚 Learning Outcomes

Through this project, I learned how to:

- Build a structured prompt evaluation system.
- Create a reusable test dataset.
- Measure prompt performance using accuracy.
- Establish a baseline before modifying a prompt.
- Make deliberate prompt changes.
- Compare different prompt versions using the same test cases.
- Detect prompt regressions through automated evaluation.
- Understand that prompt modifications should be supported by measurable results.

---

## 🔮 Future Improvements

- Add larger evaluation datasets.
- Add precision, recall, and F1-score.
- Evaluate multiple prompt versions automatically.
- Add LLM-as-a-Judge evaluation.
- Generate evaluation reports automatically.
- Visualize prompt performance using charts.
- Add more classification categories.
- Build a web-based prompt evaluation dashboard.

---

## 🎓 Key Concepts

- Prompt Engineering
- Prompt Evaluation
- Test-Driven Prompting
- Baseline Testing
- Accuracy
- Regression Testing
- Test Dataset
- Prompt Optimization
- LLM Evaluation
- Ollama
- Llama 3.2
- Python

---

## 👨‍💻 Author

**Mobeen Maroof**

GitHub Learning Journey – Prompt Engineering & AI Agents
