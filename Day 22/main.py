import json
from ollama import chat


MODEL = "llama3.2"


# Version 1: Baseline Prompt
BASELINE_PROMPT = """
Classify the following text as Positive, Negative, or Mixed.

Positive = the text expresses mainly positive feelings.
Negative = the text expresses mainly negative feelings.
Mixed = the text contains both positive and negative feelings.

Return only one label:
Positive
Negative
Mixed
"""


# Version 2: Improved Prompt
IMPROVED_PROMPT = """
You are a text classification system.

Classify the input into exactly ONE of these labels:

Positive
Negative
Mixed

Rules:
- Positive: the overall opinion is positive and there is no important negative complaint.
- Negative: the overall opinion is negative and there is no important positive opinion.
- Mixed: the text contains both meaningful positive and negative opinions.

Important:
- Read the entire sentence before deciding.
- Ignore irrelevant wording.
- Do not explain your answer.
- Return ONLY the label: Positive, Negative, or Mixed.
"""


def classify(text, prompt):
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    answer = response.message.content.strip()

    # Normalize the model response
    answer_lower = answer.lower()

    if "positive" in answer_lower:
        return "Positive"
    elif "negative" in answer_lower:
        return "Negative"
    elif "mixed" in answer_lower:
        return "Mixed"
    else:
        return "Unknown"


def evaluate(test_set, prompt):
    correct = 0
    results = []

    for test in test_set:
        prediction = classify(test["input"], prompt)
        expected = test["expected"]

        is_correct = prediction == expected

        if is_correct:
            correct += 1

        results.append({
            "input": test["input"],
            "expected": expected,
            "predicted": prediction,
            "correct": is_correct
        })

    accuracy = (correct / len(test_set)) * 100

    return accuracy, results


def print_results(title, accuracy, results):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    for item in results:
        status = "✓" if item["correct"] else "✗"

        print(f"\nInput: {item['input']}")
        print(f"Expected : {item['expected']}")
        print(f"Predicted: {item['predicted']}")
        print(f"Result   : {status}")

    print("\n" + "-" * 60)
    print(f"Accuracy: {accuracy:.2f}%")
    print("-" * 60)


def main():

    with open("test_cases.json", "r", encoding="utf-8") as file:
        test_set = json.load(file)

    print("=" * 60)
    print("       DAY 22 - PROMPT EVALUATION")
    print("=" * 60)

    # Baseline evaluation
    baseline_accuracy, baseline_results = evaluate(
        test_set,
        BASELINE_PROMPT
    )

    print_results(
        "BASELINE PROMPT",
        baseline_accuracy,
        baseline_results
    )

    # Improved prompt evaluation
    improved_accuracy, improved_results = evaluate(
        test_set,
        IMPROVED_PROMPT
    )

    print_results(
        "IMPROVED PROMPT",
        improved_accuracy,
        improved_results
    )

    print("\n" + "=" * 60)
    print("FINAL COMPARISON")
    print("=" * 60)

    print(f"Baseline Accuracy : {baseline_accuracy:.2f}%")
    print(f"Improved Accuracy : {improved_accuracy:.2f}%")
    print(
        f"Change            : "
        f"{improved_accuracy - baseline_accuracy:+.2f}%"
    )


if __name__ == "__main__":
    main()