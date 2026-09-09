from ollama import chat
from tool import calculator, current_time

MAX_STEPS = 5

TOOLS = {
    "calculator": calculator,
    "current_time": current_time,
}

SYSTEM_PROMPT = """
You are an AI assistant.

Rules:
- Think carefully.
- Use tools only when necessary.
- Never invent tool results.
- If you already have enough information, answer directly.
"""

def run_agent(messages):

    steps = 0

    while steps < MAX_STEPS:

        response = chat(
            model="llama3.2",
            messages=messages,
            tools=[calculator, current_time]
        )

        messages.append(response.message)

        # No tool call -> final answer
        if not response.message.tool_calls:
            return response.message.content

        # Execute tool(s)
        for tool_call in response.message.tool_calls:

            tool_name = tool_call.function.name
            args = tool_call.function.arguments

            if tool_name not in TOOLS:
                return f"Guardrail: Unknown tool '{tool_name}' blocked."

            try:
                if args:
                    result = TOOLS[tool_name](**args)
                else:
                    result = TOOLS[tool_name]()

            except Exception as e:
                return f"Guardrail: Tool failed ({e})"

            print(f"\nAction      : {tool_name}")
            print(f"Observation : {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )

        steps += 1

    return "Guardrail: Maximum reasoning steps reached."
