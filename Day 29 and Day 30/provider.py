import sys
import json
import os
import io
from contextlib import redirect_stdout, redirect_stderr

# Allow Python to import files from the main project folder
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from main import research_agent


def main():
    # Promptfoo passes the prompt as the first command-line argument.
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "No question provided"
        }))
        return

    question = sys.argv[1]

    try:
        # Suppress the normal CLI/debug output from main.py.
        # Promptfoo needs only the final provider output.
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            result = research_agent(question)

        # Convert the result into a clean JSON response.
        if isinstance(result, dict):
            output = result

        elif isinstance(result, str):
            try:
                output = json.loads(result)
            except json.JSONDecodeError:
                output = {
                    "summary": result,
                    "key_findings": [],
                    "evidence": [],
                    "limitations": []
                }

        else:
            output = {
                "summary": str(result),
                "key_findings": [],
                "evidence": [],
                "limitations": []
            }

        print(json.dumps(output))

    except Exception as e:
        print(json.dumps({
            "error": str(e)
        }))


if __name__ == "__main__":
    main()