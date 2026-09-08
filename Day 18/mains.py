from react_agent import run_agent, SYSTEM_PROMPT

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("=" * 60)
print("          Day 18 - ReAct Agent")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    print("\nThought : Thinking...")

    answer = run_agent(messages)

    print("\nFinal Answer:")
    print(answer)