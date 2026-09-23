# 🚀 Day 24 – DSPy Prompt Optimization

## 📌 Overview

Day 24 focuses on **automatic prompt optimization using DSPy**.

Instead of manually improving prompts, DSPy was used to optimize a sentiment classification program based on a defined evaluation metric.

The project uses the **Day 22 sentiment classification dataset** and a local **Ollama Llama 3.2** model. The dataset was divided into training and held-out test examples so that the optimized program could be evaluated on unseen data.

---

## 🎯 Objective

The main objectives of Day 24 were:

- Express the sentiment classification task using DSPy.
- Reuse the Day 22 sentiment dataset and evaluation metric.
- Split the dataset into training and held-out test data.
- Use the DSPy `BootstrapFewShot` optimizer.
- Compare the baseline classifier with the optimized classifier.
- Evaluate both approaches on the same held-out test set.
- Measure whether DSPy optimization improved the result.

---

## 🧠 Task

The system classifies text into three sentiment categories:

- **Positive**
- **Negative**
- **Mixed**

Example:

```text
Input:
The product looks great, but it stopped working after two days.

Expected:
Mixed
````

---

## 🏗️ Project Structure

```text
Day24_DSPy_Prompt_Optimization/
│
├── main.py
└── results.txt
```

---

## 🛠️ Technologies Used

* Python
* DSPy
* Ollama
* Llama 3.2
* Prompt Optimization
* Sentiment Classification

---

## 📊 Dataset

The project reuses the **20 sentiment examples from Day 22**.

The dataset was divided into:

| Dataset       | Examples |
| ------------- | -------: |
| Total         |       20 |
| Training      |       15 |
| Held-out Test |        5 |

The training examples were used by DSPy during optimization.

The held-out test examples were kept separate and used for the final evaluation.

---

## 🤖 Model

The project uses the local Ollama model:

```text
llama3.2
```

DSPy was connected to Ollama using:

```python
lm = dspy.LM("ollama_chat/llama3.2")
dspy.configure(lm=lm)
```

No OpenAI API was required.

---

## 🔧 DSPy Classifier

The sentiment classification task was expressed using a DSPy predictor:

```python
classify = dspy.Predict("text -> sentiment")
```

This defines:

```text
Input  → text
Output → sentiment
```

---

## 📏 Evaluation Metric

The evaluation metric checks whether the predicted sentiment matches the expected sentiment.

```python
def metric(example, prediction, trace=None):
    return prediction.sentiment.strip().lower() == example.sentiment.strip().lower()
```

A prediction is considered correct when:

```text
Expected Sentiment == Predicted Sentiment
```

---

## ⚙️ DSPy Optimization

The project uses the `BootstrapFewShot` optimizer:

```python
optimizer = dspy.BootstrapFewShot(
    metric=metric,
    max_bootstrapped_demos=4,
    max_labeled_demos=4
)
```

The optimizer was compiled using the training examples:

```python
optimized_classify = optimizer.compile(
    classify,
    trainset=training_examples
)
```

DSPy successfully generated:

```text
Bootstrapped 4 full traces
```

and completed the optimization process.

---

## 🧪 Evaluation Method

The baseline classifier and optimized classifier were both evaluated using the same **5 held-out test examples**.

This provides a direct comparison between:

```text
Baseline Classifier
        VS
DSPy Optimized Classifier
```

The held-out examples were not used during the optimization process.

---

## 📈 Results

The actual evaluation produced the following results:

| Method         | Correct | Accuracy |
| -------------- | ------: | -------: |
| Baseline       |   2 / 5 |   40.00% |
| DSPy Optimized |   4 / 5 |   80.00% |

### Accuracy Change

```text
Baseline Accuracy  : 40.00%
Optimized Accuracy : 80.00%
Change              : +40.00 percentage points
```

The optimized classifier correctly classified **4 of the 5 held-out examples**, compared with **2 of 5** for the baseline classifier.

---

## 🔍 Held-Out Test Results

### Baseline

```text
1. Expected: Negative → Predicted: Negative ✅
2. Expected: Positive → Predicted: Neutral  ❌
3. Expected: Mixed    → Predicted: Negative ❌
4. Expected: Positive → Predicted: Positive ✅
5. Expected: Mixed    → Predicted: Neutral  ❌
```

### DSPy Optimized

```text
1. Expected: Negative → Predicted: Negative ✅
2. Expected: Positive → Predicted: Mixed    ❌
3. Expected: Mixed    → Predicted: Mixed    ✅
4. Expected: Positive → Predicted: Positive ✅
5. Expected: Mixed    → Predicted: Mixed    ✅
```

---

## 💡 Verdict

On the 5-example held-out test set used in this experiment, the DSPy-optimized classifier achieved **80.00% accuracy**, compared with **40.00% for the baseline**, an improvement of **40 percentage points**.

This experiment demonstrates how DSPy can automatically optimize a language-model program using examples and an evaluation metric instead of relying entirely on manual prompt tuning.

---

## ▶️ Run the Project

Run:

```bash
py main.py
```

The program will:

1. Load the Day 22 dataset.
2. Create DSPy examples.
3. Split the dataset into training and held-out test sets.
4. Run the baseline classifier.
5. Define the evaluation metric.
6. Optimize the classifier using `BootstrapFewShot`.
7. Evaluate the optimized classifier.
8. Compare baseline and optimized accuracy.
9. Save the results to `results.txt`.

---

## 📄 Results File

After running the program, the evaluation results are also saved in:

```text
results.txt
```

Example:

```text
Day 24 - DSPy Prompt Optimization Results
==================================================

Total Examples: 20
Training Examples: 15
Held-out Test Examples: 5

Baseline Correct: 2/5
Baseline Accuracy: 40.00%

Optimized Correct: 4/5
Optimized Accuracy: 80.00%

Change: +40.00 percentage points
```

---

## 📸 Screenshots of Output
<img width="1304" height="988" alt="image" src="https://github.com/user-attachments/assets/ade3b080-dda6-4103-bc2c-a07f4a1c14b6" />
<img width="1443" height="952" alt="image" src="https://github.com/user-attachments/assets/9ae9a7fa-0531-4853-a0d1-bc3781ace8b8" />
<img width="1211" height="921" alt="image" src="https://github.com/user-attachments/assets/a552e700-b430-4fb2-9201-b78eeff6ddb3" />
<img width="1378" height="933" alt="image" src="https://github.com/user-attachments/assets/12875ade-c5a3-4966-ad24-960823562f30" />
<img width="1365" height="927" alt="image" src="https://github.com/user-attachments/assets/2f9d34bd-bd6b-4505-b4b0-2dd4b8d6d1e0" />
<img width="1242" height="936" alt="image" src="https://github.com/user-attachments/assets/eef9efa6-b9f6-46cd-91a7-e82af50341bd" />
<img width="1317" height="915" alt="image" src="https://github.com/user-attachments/assets/6ea10fa0-5c42-4ea3-9869-aefc742784b9" />
<img width="1364" height="939" alt="image" src="https://github.com/user-attachments/assets/3f4324a3-f5cb-44d1-a88f-641749b6943b" />
<img width="1148" height="876" alt="image" src="https://github.com/user-attachments/assets/23615052-e212-40d4-b5e4-c32efd5095a7" />

---

## 📚 Key Concepts Learned

* DSPy
* Declarative language-model programming
* Prompt optimization
* `dspy.Predict`
* `BootstrapFewShot`
* Evaluation metrics
* Training and test data separation
* Held-out evaluation
* Few-shot optimization
* Automated prompt improvement
* Local LLM evaluation with Ollama

---

## 🔮 Future Improvements

* Increase the size of the sentiment dataset.
* Add more difficult and ambiguous sentiment examples.
* Test additional Ollama models.
* Experiment with different DSPy optimizers.
* Increase the held-out test set size.
* Compare multiple prompt optimization strategies.
* Evaluate performance on a larger unseen dataset.

---

## 👨‍💻 Author

**Mobeen Maroof**

---

## ⭐ Summary

Day 24 demonstrated a complete DSPy prompt optimization workflow:

```text
Day 22 Dataset
      ↓
Training / Test Split
      ↓
DSPy Classifier
      ↓
Evaluation Metric
      ↓
BootstrapFewShot Optimization
      ↓
Held-out Test
      ↓
Baseline vs Optimized Comparison
      ↓
40% → 80%
```

The project demonstrates how prompt optimization can be treated as an **evaluated and repeatable engineering process** rather than relying only on manual prompt changes.

```
