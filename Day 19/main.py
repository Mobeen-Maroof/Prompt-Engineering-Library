from guardrails_agent import run_agent, SYSTEM_PROMPT

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("=" * 60)
print("           Day 19 - Guardrails Agent")
print("=" * 60)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = run_agent(messages)

    print("\nAssistant:")
    print(response)