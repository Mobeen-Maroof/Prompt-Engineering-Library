from ollama import chat
from tool import calculator, current_time


available_tools = {
    "calculator": calculator,
    "current_time": current_time,
}


def run_agent(messages):

    response = chat(
        model="llama3.2",
        messages=messages,
        tools=[calculator, current_time]
    )

    messages.append(response.message)

    if response.message.tool_calls:

        for tool in response.message.tool_calls:

            function = available_tools[tool.function.name]

            if tool.function.arguments:
                result = function(**tool.function.arguments)
            else:
                result = function()

            print("\nAction      :", tool.function.name)
            print("Observation :", result)

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool.function.name,
                    "content": str(result)
                }
            )

        final = chat(
            model="llama3.2",
            messages=messages
        )

        messages.append(final.message)

        return final.message.content

    return response.message.content
