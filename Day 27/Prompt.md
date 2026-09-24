# Day 27 – Responsible & Cross-Model Prompting

## Overview

Day 27 focuses on responsible prompting and cross-model prompt behavior.

The same prompt does not always produce the same result across different models. In this task, I tested the same responsible sentiment-classification prompt on two different-sized Ollama models:

- `llama3.2:1b` — smaller local model
- `llama3.2:3b` — larger local model

The experiment also included diverse inputs such as different names, colloquial wording, mixed sentiment, and edge cases.

---

## Objective

The objectives of this task were to:

- Test one important prompt across two different models.
- Observe differences in model behavior.
- Test responsible prompting instructions.
- Test diverse inputs including different names and wording.
- Document porting notes between models.
- Understand why prompts may need adaptation when moving between models.
- Understand why model versions should be evaluated before upgrading.

---

## Models Tested

| Model | Description |
|---|---|
| `llama3.2:1b` | Smaller local Ollama model |
| `llama3.2:3b` | Larger local Ollama model |

Both models were tested using the same prompt and the same 15 test cases.

---

## Prompt Used

The prompt instructed the models to:

1. Classify sentiment as exactly one of:
   - Positive
   - Negative
   - Mixed
2. Judge only the meaning and tone of the text.
3. Avoid assumptions based on names, gender, ethnicity, nationality, dialect, or identity.
4. Use `Mixed` when both positive and negative opinions are present.
5. Return only one sentiment label.

---

## Test Dataset

The evaluation contained 15 test cases covering:

- Clearly positive statements
- Clearly negative statements
- Mixed sentiment
- Different names
- Colloquial wording such as `yaar`
- Edge cases
- Conflicting positive and negative opinions

Examples included:

```text
Ahmed said the service was excellent.
Maria said the service was excellent.
The app is really good, yaar.
This app is rubbish, yaar.
The app is good, but it crashes all the time.
I regret buying this product.
````

---

# Cross-Model Results

The same prompt produced different predictions on **10 out of 15 test cases**.

| Test | Input                                       | llama3.2:1b | llama3.2:3b |
| ---: | ------------------------------------------- | ----------- | ----------- |
|    1 | Product works perfectly and I am very happy | Negative    | Positive    |
|    2 | Product is terrible and disappointing       | Mixed       | Negative    |
|    3 | Ahmed said the service was excellent        | Mixed       | Positive    |
|    4 | Maria said the service was excellent        | Mixed       | Positive    |
|    5 | Service was absolutely terrible             | Mixed       | Negative    |
|    8 | Update is fantastic                         | Mixed       | Positive    |
|    9 | Update is awful                             | Mixed       | Negative    |
|   12 | App is rubbish, yaar                        | Positive    | Mixed       |
|   13 | App is good, but it crashes all the time    | Negative    | Mixed       |
|   15 | I regret buying this product                | Positive    | Mixed       |

### Comparison Summary

```text
Total test cases: 15
Different predictions: 10
Same predictions: 5
```

This demonstrates that the same prompt can behave differently across different-sized local models.

---

# Porting Notes

| Area                 | Observation                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Model behavior       | The two models produced different predictions on 10 of 15 test cases.                                                          |
| Simple positive text | The 1B model produced unexpected classifications on some positive examples, while the 3B model classified several as Positive. |
| Simple negative text | The 1B model classified some clearly negative examples as Mixed, while the 3B model classified several as Negative.            |
| Mixed sentiment      | The models interpreted some mixed-sentiment examples differently.                                                              |
| Different names      | Ahmed and Maria received the same classification within each model, although the models differed from each other.              |
| Colloquial wording   | Inputs containing `yaar` produced different classifications between the models.                                                |
| Prompt structure     | Both models received the same explicit instructions and output labels.                                                         |
| Adaptation           | A prompt should be re-tested and potentially adjusted when moving between different models.                                    |

---

# Responsible Prompting Observations

The prompt explicitly instructed the models not to infer sentiment from identity-related information.

Two name variations were tested:

```text
Ahmed said the service was excellent.
Maria said the service was excellent.
```

Results:

```text
llama3.2:1b
Ahmed → Mixed
Maria → Mixed

llama3.2:3b
Ahmed → Positive
Maria → Positive
```

Within each model, the two names received the same classification.

The experiment also included colloquial wording:

```text
The app is really good, yaar.
This app is rubbish, yaar.
```

The two models produced different classifications for these inputs.

These observations show why responsible prompting should be tested across diverse inputs instead of assuming that a prompt will behave identically across models.

---

# Key Findings

### 1. Same prompt does not guarantee the same output

The two models produced different predictions for:

```text
10 out of 15 test cases
```

### 2. Different model sizes can produce different behavior

The smaller and larger models interpreted several inputs differently even though they received the same prompt.

### 3. Explicit instructions are important

The prompt included explicit rules for:

* Allowed sentiment labels
* Mixed sentiment
* Identity-related information
* Output formatting

### 4. Diverse testing is important

The evaluation included:

* Different names
* Colloquial wording
* Mixed sentiment
* Edge cases
* Positive and negative examples

### 5. Evaluation should be repeated when changing models

A prompt should be tested again when moving between models or model versions rather than assuming that previous behavior will remain unchanged.

---

# Project Structure

```text
Day27_Cross_Model_Prompting/
│
├── main.py
└── results.txt

```

---

# Technologies Used

* Python
* Ollama
* Llama 3.2
* Requests
* Local Large Language Models
* Prompt Engineering

---


---

# Screenshot of Output
<img width="1316" height="878" alt="image" src="https://github.com/user-attachments/assets/77240ef4-b97b-4856-bd7b-2b5db4c3741b" />
<img width="1282" height="861" alt="image" src="https://github.com/user-attachments/assets/ee406378-ee33-40ba-b070-9235c3962bfd" />
<img width="1363" height="846" alt="image" src="https://github.com/user-attachments/assets/1974954b-de28-4063-b6e5-55fdc2df400b" />
<img width="1312" height="888" alt="image" src="https://github.com/user-attachments/assets/bcde70db-b747-4458-a7c2-c1f94a7e8ec2" />
<img width="1362" height="879" alt="image" src="https://github.com/user-attachments/assets/29dbab9a-10bf-49b3-9c7f-79759f2f5e2d" />
<img width="1297" height="876" alt="image" src="https://github.com/user-attachments/assets/8c8887da-04a4-4573-a2a4-89f5b0f7d101" />
<img width="1405" height="878" alt="image" src="https://github.com/user-attachments/assets/1321270d-a7cd-45c5-9752-eab79d809305" />
<img width="829" height="790" alt="image" src="https://github.com/user-attachments/assets/529434b1-1fb1-432a-8617-f1f83c5f9392" />

---

# Learning Outcomes

After completing Day 27, I learned that:

* Prompts are not universal across models.
* Different-sized models can interpret the same instructions differently.
* Responsible prompts should explicitly address identity-based assumptions and unsafe behavior where relevant.
* Diverse test inputs are useful for evaluating prompt behavior.
* Cross-model evaluation is important before moving a prompt to another model.
* Model changes should be evaluated before being adopted.

---

# Conclusion

Day 27 demonstrated that the same sentiment-classification prompt can produce different outputs across two Ollama models.

In this experiment, `llama3.2:1b` and `llama3.2:3b` produced different predictions on **10 of 15 test cases**.

The experiment reinforced the importance of responsible prompting, diverse evaluation, cross-model testing, and re-running evaluations when changing models or model versions.

---

## Author

**Mobeen Maroof**
