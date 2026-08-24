from tool import calculator, get_current_time

print("=" * 50)
print("        ReAct Agent Demo")
print("=" * 50)

# Multi-step Question
question = "What is (25 + 15) × 4?"

print("\nQuestion:")
print(question)

# Thought
print("\nThought:")
print("I need to calculate (25 + 15) × 4.")

# Action
expression = "(25+15)*4"
print("\nAction:")
print(f'calculator("{expression}")')

# Observation
result = calculator(expression)
print("\nObservation:")
print(result)

# Final Answer
print("\nAnswer:")
print(f"The answer is {result}.")