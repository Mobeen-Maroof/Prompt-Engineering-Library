from ollama import chat
from tool import calculator, current_time

TOOLS = {
    "calculator": calculator,
    "current_time": current_time,
}

SYSTEM_PROMPT = """
You are a ReAct AI Agent.

Follow this process:

Thought:
Think about the user's request.

Action:
Choose one tool if needed.

Observation:
Use the tool result.

Repeat if necessary.

When you have enough information, provide the Final Answer.

Never invent tool results.
"""

def run_agent(messages):

    while True:

        response = chat(
            model="llama3.2",
            messages=messages,
            tools=[calculator, current_time]
        )

        messages.append(response.message)

        # No tool requested -> final answer
        if not response.message.tool_calls:
            return response.message.content

        # Execute tool(s)
        for tool_call in response.message.tool_calls:

            tool_name = tool_call.function.name
            args = tool_call.function.arguments

            tool = TOOLS[tool_name]

            if args:
                result = tool(**args)
            else:
                result = tool()

            print(f"\nAction      : {tool_name}")
            print(f"Observation : {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )
