from ollama import chat
from tool import calculator, current_time

available_tools = {
    "calculator": calculator,
    "current_time": current_time,
}

messages = []

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    response = chat(
        model="llama3.2",
        messages=messages,
        tools=[calculator, current_time],
    )

    messages.append(response.message)

    if response.message.tool_calls:

        for tool in response.message.tool_calls:

            function_name = tool.function.name
            arguments = tool.function.arguments

            function = available_tools.get(function_name)

            if function:

                if arguments:
                    result = function(**arguments)
                else:
                    result = function()

                print(f"\nTool Used : {function_name}")
                print("Tool Result:", result)

                messages.append(
                    {
                        "role": "tool",
                        "tool_name": function_name,
                        "content": str(result),
                    }
                )

        final = chat(
            model="llama3.2",
            messages=messages,
        )

        print("\nAssistant:", final.message.content)

        messages.append(final.message)

    else:

        print("\nAssistant:", response.message.content)
