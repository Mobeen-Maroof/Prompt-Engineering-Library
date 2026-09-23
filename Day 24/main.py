import dspy

# ============================================
# 1. Connect DSPy to local Ollama
# ============================================

lm = dspy.LM("ollama_chat/llama3.2")
dspy.configure(lm=lm)


# ============================================
# 2. DSPy Sentiment Classifier
# ============================================

classify = dspy.Predict("text -> sentiment")


# ============================================
# 3. Day 22 Dataset
# ============================================

dataset = [
    {
        "text": "The product is absolutely fantastic and works perfectly.",
        "sentiment": "Positive"
    },
    {
        "text": "I am extremely disappointed with this purchase.",
        "sentiment": "Negative"
    },
    {
        "text": "The delivery was quick, but the product quality was terrible.",
        "sentiment": "Mixed"
    },
    {
        "text": "I expected more, but overall I am happy with it.",
        "sentiment": "Positive"
    },
    {
        "text": "The design is beautiful, although the battery life is poor.",
        "sentiment": "Mixed"
    },
    {
        "text": "Nothing about this product impressed me.",
        "sentiment": "Negative"
    },
    {
        "text": "It is not bad at all. I actually really like it.",
        "sentiment": "Positive"
    },
    {
        "text": "The service was helpful, but the response took too long.",
        "sentiment": "Mixed"
    },
    {
        "text": "I would definitely recommend this product to my friends.",
        "sentiment": "Positive"
    },
    {
        "text": "I regret buying this product.",
        "sentiment": "Negative"
    },
    {
        "text": "The price is reasonable and the quality is excellent.",
        "sentiment": "Positive"
    },
    {
        "text": "The product looks great, but it stopped working after two days.",
        "sentiment": "Mixed"
    },
    {
        "text": "The item arrived late and was damaged.",
        "sentiment": "Negative"
    },
    {
        "text": "The camera quality is excellent, but the software is frustrating.",
        "sentiment": "Mixed"
    },
    {
        "text": "I have no complaints. Everything works as expected.",
        "sentiment": "Positive"
    },
    {
        "text": "The product is expensive, unreliable, and disappointing.",
        "sentiment": "Negative"
    },
    {
        "text": "I like the product overall, even though the packaging was poor.",
        "sentiment": "Positive"
    },
    {
        "text": "The food was delicious, but the restaurant service was very slow.",
        "sentiment": "Mixed"
    },
    {
        "text": "The quality is better than I expected.",
        "sentiment": "Positive"
    },
    {
        "text": "The product has some useful features, but it is difficult to use.",
        "sentiment": "Mixed"
    },
]


# ============================================
# 4. Convert dataset to DSPy Examples
# ============================================

examples = [
    dspy.Example(
        text=item["text"],
        sentiment=item["sentiment"]
    ).with_inputs("text")
    for item in dataset
]


# ============================================
# 5. Split into Training and Held-out Test
# ============================================

training_examples = examples[:15]
test_examples = examples[15:]

print("Total examples:", len(examples))
print("Training examples:", len(training_examples))
print("Held-out test examples:", len(test_examples))


# ============================================
# 6. Define Evaluation Metric
# ============================================

def metric(example, prediction, trace=None):
    """
    Returns True when the predicted sentiment
    exactly matches the expected sentiment.
    """
    return prediction.sentiment.strip().lower() == example.sentiment.strip().lower()


# ============================================
# 7. Calculate Baseline Accuracy
# ============================================

print("\n" + "=" * 60)
print("BASELINE EVALUATION")
print("=" * 60)

baseline_correct = 0

for example in test_examples:
    prediction = classify(text=example.text)

    is_correct = metric(example, prediction)

    if is_correct:
        baseline_correct += 1

    print("\nText:", example.text)
    print("Expected:", example.sentiment)
    print("Predicted:", prediction.sentiment)
    print("Correct:", is_correct)


baseline_accuracy = (
    baseline_correct / len(test_examples)
) * 100

print("\nBaseline Correct:", baseline_correct)
print("Baseline Accuracy:", f"{baseline_accuracy:.2f}%")

# ============================================
# 8. DSPy Prompt Optimization
# ============================================

print("\n" + "=" * 60)
print("DSPy PROMPT OPTIMIZATION")
print("=" * 60)

optimizer = dspy.BootstrapFewShot(
    metric=metric,
    max_bootstrapped_demos=4,
    max_labeled_demos=4
)

optimized_classify = optimizer.compile(
    classify,
    trainset=training_examples
)

print("\nDSPy optimization completed successfully!")

# ============================================
# 9. Evaluate Optimized Classifier
# ============================================

print("\n" + "=" * 60)
print("OPTIMIZED DSPy EVALUATION")
print("=" * 60)

optimized_correct = 0

for example in test_examples:
    prediction = optimized_classify(text=example.text)

    is_correct = metric(example, prediction)

    if is_correct:
        optimized_correct += 1

    print("\nText:", example.text)
    print("Expected:", example.sentiment)
    print("Predicted:", prediction.sentiment)
    print("Correct:", is_correct)


optimized_accuracy = (
    optimized_correct / len(test_examples)
) * 100

print("\nOptimized Correct:", optimized_correct)
print("Optimized Accuracy:", f"{optimized_accuracy:.2f}%")

# ============================================
# 10. Final Comparison
# ============================================

change = optimized_accuracy - baseline_accuracy

print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)

print("Baseline Accuracy :", f"{baseline_accuracy:.2f}%")
print("Optimized Accuracy:", f"{optimized_accuracy:.2f}%")
print("Change             :", f"{change:+.2f}%")

# ============================================
# 11. Save Results
# ============================================

with open("results.txt", "w", encoding="utf-8") as file:
    file.write("Day 24 - DSPy Prompt Optimization Results\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Examples: {len(examples)}\n")
    file.write(f"Training Examples: {len(training_examples)}\n")
    file.write(f"Held-out Test Examples: {len(test_examples)}\n\n")

    file.write(f"Baseline Correct: {baseline_correct}/{len(test_examples)}\n")
    file.write(f"Baseline Accuracy: {baseline_accuracy:.2f}%\n\n")

    file.write(f"Optimized Correct: {optimized_correct}/{len(test_examples)}\n")
    file.write(f"Optimized Accuracy: {optimized_accuracy:.2f}%\n\n")

    file.write(f"Change: {change:+.2f} percentage points\n")

print("\nResults saved to results.txt")