from tool import calculator

MAX_STEPS = 5
STEP_BUDGET = 5

allowed_tools = ["calculator"]

question = "Calculate (15 + 25) * 3"

print("=" * 60)
print(" Day 19 - ReAct Agent with Guardrails")
print("=" * 60)

print("\nQuestion:")
print(question)

steps = 0

while steps < MAX_STEPS:

    print(f"\nStep {steps + 1}")

    print("Thought:")
    print("I should use the calculator tool.")

    tool = "calculator"

    if tool not in allowed_tools:
        print("Observation:")
        print("Tool not allowed.")
        break

    print("Action:")
    print('calculator("(15+25)*3")')

    result = calculator("(15+25)*3")

    print("Observation:")
    print(result)

    print("Reflection:")
    print("The calculation completed successfully. No further steps are required.")

    print("\nFinal Answer:")
    print(result)

    break

    steps += 1

if steps >= STEP_BUDGET:
    print("\nStopped: Step budget exceeded.")