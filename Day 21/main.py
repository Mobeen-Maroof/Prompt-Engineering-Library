from react_agent import run_agent
from guardrails_agent import validate_input
from agents import research_agent, writer_agent

messages = [
    {
        "role": "system",
        "content": """
You are an AI Capstone Agent.

Rules:
- Answer normal questions directly.
- Use tools whenever needed.
- Never invent tool results.
- If the user asks to research a topic, first gather research notes, then write the final response.
"""
    }
]

print("=" * 65)
print("      Day 21 - AI Capstone Agent")
print("=" * 65)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    # ---------------- Guardrails ----------------

    valid, message = validate_input(user_input)

    if not valid:
        print("\nGuardrail:", message)
        continue

    # ------------ Multi-Agent Mode -------------

    if user_input.lower().startswith("research:"):

        topic = user_input.replace("research:", "").strip()

        print("\nResearch Agent is working...")

        notes = research_agent(topic)

        print("\n==============================")
        print("Research Notes")
        print("==============================")
        print(notes)

        print("\nWriter Agent is writing...")

        final_answer = writer_agent(topic, notes)

        print("\n==============================")
        print("Final Answer")
        print("==============================")
        print(final_answer)

        continue

    # ---------------- ReAct + Tool Calling ----------------

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    answer = run_agent(messages)

    print("\nAssistant:")
    print(answer)
