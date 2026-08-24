from tool import calculator, get_current_time

def execute_tool(tool_name, argument=None):

    if tool_name == "calculator":
        return calculator(argument)

    elif tool_name == "get_current_time":
        return get_current_time()

    else:
        return "Tool Not Found"


print("Question 1")
print("User: What is 25 * 8?")
print("Tool:", execute_tool("calculator", "25*8"))

print()

print("Question 2")
print("User: What is 150 / 5?")
print("Tool:", execute_tool("calculator", "150/5"))

print()

print("Question 3")
print("User: What time is it?")
print("Tool:", execute_tool("get_current_time"))

print()

print("Question 4")
print("User: Calculate (20+30)*5")
print("Tool:", execute_tool("calculator", "(20+30)*5"))

print()

print("Question 5")
print("User: Hello")
print("Assistant: Hello! How can I help you?")