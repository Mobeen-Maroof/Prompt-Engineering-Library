from tool import calculator, get_current_time

MAX_STEPS = 5
STEP_BUDGET = 5

ALLOWED_TOOLS = ["calculator", "get_current_time"]

def run_agent(question):

    print("=" * 60)
    print("Week 3 Capstone Agent")
    print("=" * 60)

    print("\nQuestion:")
    print(question)

    steps = 0

    while steps < MAX_STEPS:

        print(f"\nStep {steps+1}")

        # Calculator Task
        if "calculate" in question.lower():

            print("Thought:")
            print("The user wants a calculation.")

            tool = "calculator"

            if tool not in ALLOWED_TOOLS:
                print("Observation:")
                print("Tool not allowed.")
                return

            expression = question.lower().replace("calculate", "").strip()

            print("\nAction:")
            print(f'calculator("{expression}")')

            result = calculator(expression)

            print("\nObservation:")
            print(result)

            print("\nReflection:")
            print("The calculation completed successfully.")

            print("\nFinal Answer:")
            print(result)

            return

        # Time Task
        elif "time" in question.lower():

            print("Thought:")
            print("The user wants the current time.")

            tool = "get_current_time"

            print("\nAction:")
            print("get_current_time()")

            result = get_current_time()

            print("\nObservation:")
            print(result)

            print("\nReflection:")
            print("Current time returned successfully.")

            print("\nFinal Answer:")
            print(result)

            return

        else:

            print("Thought:")
            print("No suitable tool is available.")

            print("\nReflection:")
            print("Stop execution gracefully.")

            print("\nFinal Result:")
            print("Unable to complete the request.")

            return

        steps += 1

run_agent("Calculate (25+15)*4")

print("\n")

run_agent("Find the happiness index of dreams.")