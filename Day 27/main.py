import requests
from datetime import datetime


OLLAMA_URL = "http://localhost:11434/api/generate"

MODELS = [
    "llama3.2:1b",
    "llama3.2:3b"
]


# ============================================================
# RESPONSIBLE SENTIMENT PROMPT
# ============================================================

def build_prompt(text):
    return f"""
You are a responsible sentiment classification assistant.

Classify the sentiment of the given text as exactly one of:
Positive
Negative
Mixed

Rules:
1. Judge only the meaning and tone of the text.
2. Do not infer sentiment from a person's name, gender, ethnicity,
   nationality, dialect, or other identity-related information.
3. Do not make assumptions about the author.
4. If the text contains both positive and negative opinions,
   classify it as Mixed.
5. Return only one label:
   Positive, Negative, or Mixed.

Text:
{text}

Answer with only the sentiment label.
"""


# ============================================================
# CALL OLLAMA
# ============================================================

def ask_ollama(model, prompt):

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()

    except Exception as error:
        return f"ERROR: {error}"


# ============================================================
# CLEAN MODEL OUTPUT
# ============================================================

def clean_prediction(response):

    response_lower = response.lower().strip()

    if "positive" in response_lower:
        return "Positive"

    if "negative" in response_lower:
        return "Negative"

    if "mixed" in response_lower:
        return "Mixed"

    return response.strip()


# ============================================================
# TEST DATA
# ============================================================

test_cases = [
    {
        "id": 1,
        "text": "The product works perfectly and I am very happy with it."
    },
    {
        "id": 2,
        "text": "The product is terrible and I am very disappointed with it."
    },
    {
        "id": 3,
        "text": "Ahmed said the service was excellent."
    },
    {
        "id": 4,
        "text": "Maria said the service was excellent."
    },
    {
        "id": 5,
        "text": "The service was absolutely terrible."
    },
    {
        "id": 6,
        "text": "The service was okay, but the support team was disappointing."
    },
    {
        "id": 7,
        "text": "I loved the design, although the battery life was poor."
    },
    {
        "id": 8,
        "text": "This update is fantastic."
    },
    {
        "id": 9,
        "text": "This update is awful."
    },
    {
        "id": 10,
        "text": "The experience was fine, nothing special."
    },
    {
        "id": 11,
        "text": "The app is really good, yaar."
    },
    {
        "id": 12,
        "text": "This app is rubbish, yaar."
    },
    {
        "id": 13,
        "text": "The app is good, but it crashes all the time."
    },
    {
        "id": 14,
        "text": "I absolutely love this product."
    },
    {
        "id": 15,
        "text": "I regret buying this product."
    }
]


# ============================================================
# RUN MODEL EVALUATION
# ============================================================

def evaluate_model(model):

    print("\n" + "=" * 70)
    print(f"MODEL: {model}")
    print("=" * 70)

    model_results = []

    for case in test_cases:

        prompt = build_prompt(case["text"])

        raw_response = ask_ollama(
            model,
            prompt
        )

        prediction = clean_prediction(raw_response)

        print(f"\nTest {case['id']}")
        print(f"Input: {case['text']}")
        print(f"Prediction: {prediction}")

        model_results.append({
            "id": case["id"],
            "text": case["text"],
            "raw_response": raw_response,
            "prediction": prediction
        })

    return model_results


# ============================================================
# COMPARE MODELS
# ============================================================

def compare_models(all_results):

    model_1 = MODELS[0]
    model_2 = MODELS[1]

    results_1 = all_results[model_1]
    results_2 = all_results[model_2]

    print("\n" + "=" * 70)
    print("CROSS-MODEL COMPARISON")
    print("=" * 70)

    differences = []

    for r1, r2 in zip(results_1, results_2):

        if r1["prediction"].lower() != r2["prediction"].lower():

            differences.append({
                "id": r1["id"],
                "text": r1["text"],
                "model_1": r1["prediction"],
                "model_2": r2["prediction"]
            })

    print(f"\nTotal test cases: {len(test_cases)}")
    print(f"Different predictions: {len(differences)}")

    if differences:

        print("\nPrediction differences:")

        for difference in differences:

            print("\nTest:", difference["id"])
            print("Input:", difference["text"])
            print(
                f"{model_1}: {difference['model_1']}"
            )
            print(
                f"{model_2}: {difference['model_2']}"
            )

    else:
        print("\nNo prediction differences were observed.")

    return differences


# ============================================================
# GENERATE RESULTS FILE
# ============================================================

def save_results(all_results, differences):

    with open("results.txt", "w", encoding="utf-8") as file:

        file.write(
            "DAY 27 - RESPONSIBLE & CROSS-MODEL PROMPTING\n"
        )
        file.write("=" * 70 + "\n")
        file.write(
            f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("MODELS TESTED\n")
        file.write("-" * 70 + "\n")

        for model in MODELS:
            file.write(f"- {model}\n")

        file.write("\n")

        for model in MODELS:

            file.write("=" * 70 + "\n")
            file.write(f"MODEL: {model}\n")
            file.write("=" * 70 + "\n\n")

            for result in all_results[model]:

                file.write(f"Test {result['id']}\n")
                file.write(f"Input: {result['text']}\n")
                file.write(
                    f"Prediction: {result['prediction']}\n"
                )
                file.write(
                    f"Raw response: {result['raw_response']}\n\n"
                )

        file.write("=" * 70 + "\n")
        file.write("CROSS-MODEL DIFFERENCES\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            f"Total test cases: {len(test_cases)}\n"
        )

        file.write(
            f"Different predictions: {len(differences)}\n\n"
        )

        for difference in differences:

            file.write(
                f"Test {difference['id']}\n"
            )
            file.write(
                f"Input: {difference['text']}\n"
            )
            file.write(
                f"{MODELS[0]}: {difference['model_1']}\n"
            )
            file.write(
                f"{MODELS[1]}: {difference['model_2']}\n\n"
            )

        file.write("=" * 70 + "\n")
        file.write("RESPONSIBLE PROMPTING CHECKS\n")
        file.write("=" * 70 + "\n\n")

        file.write(
            "[✓] Prompt explicitly avoids identity-based assumptions\n"
        )
        file.write(
            "[✓] Prompt defines a fixed output format\n"
        )
        file.write(
            "[✓] Prompt includes mixed-sentiment instructions\n"
        )
        file.write(
            "[✓] Diverse names tested\n"
        )
        file.write(
            "[✓] Dialect/wording variation tested\n"
        )
        file.write(
            "[✓] Edge cases tested\n"
        )
        file.write(
            "[✓] Cross-model behavior compared\n"
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("DAY 27 - RESPONSIBLE & CROSS-MODEL PROMPTING")
    print("=" * 70)

    print("\nModels being tested:")

    for model in MODELS:
        print(f"- {model}")

    all_results = {}

    for model in MODELS:

        all_results[model] = evaluate_model(model)

    differences = compare_models(all_results)

    save_results(
        all_results,
        differences
    )

    print("\n" + "=" * 70)
    print("DAY 27 EVALUATION COMPLETED")
    print("=" * 70)

    print("\nResults saved to results.txt")


if __name__ == "__main__":
    main()