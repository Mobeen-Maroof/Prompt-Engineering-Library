import json
import requests

from prompts import (
    SYSTEM_PROMPT,
    TOOL_SELECTION_PROMPT,
    FINAL_ANSWER_PROMPT
)

from tools import (
    research_tool,
    calculator_tool
)


# ============================================================
# CONFIGURATION
# ============================================================

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"


# ============================================================
# OLLAMA REQUEST
# ============================================================

def ask_ollama(messages, temperature=0):
    """
    Send a conversation to the local Ollama model.
    """

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]


# ============================================================
# SECURITY GUARDRAILS
# ============================================================

SUSPICIOUS_PATTERNS = [
    "ignore all previous instructions",
    "ignore previous instructions",
    "ignore all prior instructions",
    "ignore prior instructions",
    "disregard previous instructions",
    "disregard all previous instructions",
    "reveal the system prompt",
    "show the system prompt",
    "print the system prompt",
    "reveal system instructions",
    "show system instructions",
    "reveal security rules",
    "show security rules",
    "reveal internal instructions",
    "show internal instructions",
    "execute operating system command",
    "execute os command",
    "run operating system command",
    "execute commands",
    "__import__",
    "os.system",
    "subprocess",
    "shell command",
]


def contains_suspicious_instruction(text):
    """
    Check text for known prompt-injection or tool-abuse patterns.
    """

    if not isinstance(text, str):
        return False

    text_lower = text.lower()

    for pattern in SUSPICIOUS_PATTERNS:

        if pattern.lower() in text_lower:
            return True

    return False


def input_guardrail(question):
    """
    Detect obvious prompt-injection and tool-abuse attempts
    coming directly from the user.
    """

    if contains_suspicious_instruction(question):

        return False, (
            "Request blocked by security guardrail. "
            "The request contains a suspicious instruction "
            "or unauthorized tool-use pattern."
        )

    return True, ""


# ============================================================
# RETRIEVED DATA SECURITY
# ============================================================

def sanitize_retrieved_data(tool_result):
    """
    Treat retrieved documents as untrusted data.

    If suspicious instructions are found inside retrieved
    content, remove those instruction lines before the content
    is passed to the final-answer model.
    """

    if not isinstance(tool_result, str):
        return str(tool_result), False

    lines = tool_result.splitlines()

    safe_lines = []
    blocked = False

    for line in lines:

        if contains_suspicious_instruction(line):

            blocked = True

            safe_lines.append(
                "[BLOCKED UNTRUSTED INSTRUCTION]"
            )

        else:

            safe_lines.append(line)

    return "\n".join(safe_lines), blocked


# ============================================================
# JSON EXTRACTION
# ============================================================

def extract_json(text):
    """
    Extract a JSON object from model output.
    """

    if not isinstance(text, str):
        return None

    text = text.strip()

    # First try the complete response.
    try:

        return json.loads(text)

    except json.JSONDecodeError:
        pass

    # Try to find the JSON object inside additional text.
    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1 and end > start:

        possible_json = text[start:end + 1]

        try:

            return json.loads(possible_json)

        except json.JSONDecodeError:

            return None

    return None


# ============================================================
# STRUCTURED OUTPUT VALIDATION
# ============================================================

def validate_output(data):
    """
    Validate and normalize the required ResearchResponse structure.

    Required fields:

    summary:
        string

    key_findings:
        list of strings

    evidence:
        list of strings

    limitations:
        list of strings
    """

    if not isinstance(data, dict):
        return None

    required_fields = [
        "summary",
        "key_findings",
        "evidence",
        "limitations"
    ]

    # Check that every required field exists.
    for field in required_fields:

        if field not in data:

            return None

    # Summary must be a string.
    if not isinstance(data["summary"], str):

        return None

    # These fields must be lists of strings.
    for field in [
        "key_findings",
        "evidence",
        "limitations"
    ]:

        # Normalize a single string into a list.
        if isinstance(data[field], str):

            data[field] = [
                data[field]
            ]

        if not isinstance(data[field], list):

            return None

        if not all(
            isinstance(item, str)
            for item in data[field]
        ):

            return None

    return data


# ============================================================
# SAFE FALLBACK RESPONSE
# ============================================================

def create_safe_response(
    summary,
    key_findings=None,
    evidence=None,
    limitations=None
):
    """
    Always return a valid ResearchResponse structure.
    """

    return {
        "summary": summary,

        "key_findings": (
            key_findings
            if key_findings is not None
            else []
        ),

        "evidence": (
            evidence
            if evidence is not None
            else []
        ),

        "limitations": (
            limitations
            if limitations is not None
            else []
        )
    }


# ============================================================
# TOOL SELECTION
# ============================================================

def select_tool(question):
    """
    Ask the model to decide which approved tool should be used.

    This is model-driven tool selection.
    """

    prompt = TOOL_SELECTION_PROMPT + question

    response = ask_ollama(
        [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    decision = extract_json(response)

    if not decision:

        return {
            "tool": "none",
            "argument": ""
        }

    tool = decision.get(
        "tool",
        "none"
    )

    argument = decision.get(
        "argument",
        ""
    )

    allowed_tools = {
        "research_tool",
        "calculator_tool",
        "none"
    }

    if tool not in allowed_tools:

        return {
            "tool": "none",
            "argument": ""
        }

    # Never allow suspicious content to become a tool argument.
    if contains_suspicious_instruction(
        str(argument)
    ):

        return {
            "tool": "none",
            "argument": ""
        }

    return {
        "tool": tool,
        "argument": str(argument)
    }


# ============================================================
# TOOL EXECUTION
# ============================================================

def execute_tool(tool_name, argument):
    """
    Execute only approved tools.
    """

    if tool_name == "research_tool":

        return research_tool(argument)

    if tool_name == "calculator_tool":

        return calculator_tool(argument)

    return ""


# ============================================================
# FINAL RESPONSE
# ============================================================

def generate_final_answer(
    question,
    tool_name,
    tool_result
):
    """
    Generate the final structured response.

    Retrieved content is checked and sanitized before
    being sent to the model.
    """

    # --------------------------------------------------------
    # SECURITY CHECK ON RETRIEVED DATA
    # --------------------------------------------------------

    safe_tool_result, injection_detected = (
        sanitize_retrieved_data(tool_result)
    )

    # --------------------------------------------------------
    # INDIRECT PROMPT-INJECTION DEFENSE
    # --------------------------------------------------------

    if injection_detected:

        return create_safe_response(

            summary=(
                "The retrieved content contained "
                "an untrusted instruction that was blocked."
            ),

            key_findings=[
                "Retrieved documents are treated as untrusted data.",
                "Instructions inside retrieved documents were not followed."
            ],

            evidence=[
                "The research tool returned untrusted retrieved data."
            ],

            limitations=[
                "A prompt-injection pattern was detected "
                "inside retrieved content.",
                "The suspicious instruction was blocked before "
                "the final response was generated."
            ]
        )

    # --------------------------------------------------------
    # BUILD FINAL RESPONSE PROMPT
    # --------------------------------------------------------

    prompt = FINAL_ANSWER_PROMPT

    prompt = prompt.replace(
        "{question}",
        question
    )

    prompt = prompt.replace(
        "{tool}",
        tool_name
    )

    prompt = prompt.replace(
        "{tool_result}",
        safe_tool_result
    )

    # --------------------------------------------------------
    # ASK MODEL
    # --------------------------------------------------------

    response = ask_ollama(
        [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # --------------------------------------------------------
    # PARSE MODEL RESPONSE
    # --------------------------------------------------------

    data = extract_json(response)

    validated_data = validate_output(data)

    # --------------------------------------------------------
    # INVALID OUTPUT FALLBACK
    # --------------------------------------------------------

    if validated_data is None:

        return create_safe_response(

            summary=(
                "The model returned an invalid "
                "structured response."
            ),

            key_findings=[],

            evidence=[],

            limitations=[
                "The model output did not match "
                "the required schema."
            ]
        )

    # --------------------------------------------------------
    # FINAL OUTPUT SECURITY CHECK
    # --------------------------------------------------------

    # Check only for actual disclosure of protected information.
    # Do not scan the entire JSON blindly: legitimate research topics
    # such as "Prompt Injection" and "AI Security" may contain the word
    # "security" without exposing any protected instructions.
    protected_disclosure_patterns = [
        "here is the system prompt",
        "here's the system prompt",
        "the system prompt is:",
        "system prompt:",
        "here are the system instructions",
        "here's the system instructions",
        "the system instructions are:",
        "security rules are:",
        "here are the security rules",
        "here's the security rules",
    ]

    response_text = json.dumps(
        validated_data
    ).lower()

    if any(
        pattern in response_text
        for pattern in protected_disclosure_patterns
    ):

        return create_safe_response(

            summary=(
                "The response was blocked by "
                "the output security check."
            ),

            key_findings=[],

            evidence=[],

            limitations=[
                "The generated response appeared to "
                "contain protected instruction disclosure."
            ]
        )

    return validated_data


# ============================================================
# AGENT
# ============================================================

def research_agent(question):

    # --------------------------------------------------------
    # INPUT SECURITY CHECK
    # --------------------------------------------------------

    allowed, security_message = (
        input_guardrail(question)
    )

    if not allowed:

        print("\n[SECURITY GUARDRAIL]")

        print(security_message)

        return create_safe_response(

            summary=(
                "Request blocked by security guardrail."
            ),

            limitations=[
                security_message
            ]
        )

    # --------------------------------------------------------
    # AGENT HEADER
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("SECURE RESEARCH ASSISTANT")
    print("=" * 60)

    print("\nUser Question:")
    print(question)

    # --------------------------------------------------------
    # MODEL-DRIVEN TOOL SELECTION
    # --------------------------------------------------------

    print(
        "\n[1] Asking model to select a tool..."
    )

    decision = select_tool(question)

    print("\nModel Decision:")

    print(
        json.dumps(
            decision,
            indent=2
        )
    )

    tool_name = decision["tool"]
    argument = decision["argument"]

    # --------------------------------------------------------
    # TOOL EXECUTION
    # --------------------------------------------------------

    if tool_name == "none":

        tool_result = (
            "No tool was required for this question."
        )

    else:

        print(
            f"\n[2] Executing tool: {tool_name}"
        )

        tool_result = execute_tool(
            tool_name,
            argument
        )

        print("\nTool Result:")
        print(tool_result)

    # --------------------------------------------------------
    # FINAL RESPONSE
    # --------------------------------------------------------

    print(
        "\n[3] Asking model to generate final response..."
    )

    final_response = generate_final_answer(
        question,
        tool_name,
        tool_result
    )

    print("\nFinal Response:")

    print(
        json.dumps(
            final_response,
            indent=2
        )
    )

    return final_response


# ============================================================
# INDIRECT PROMPT INJECTION TEST
# ============================================================

def test_indirect_prompt_injection():

    print("\n" + "=" * 60)
    print("INDIRECT PROMPT INJECTION SECURITY TEST")
    print("=" * 60)

    attack_question = (
        "Tell me about research assistants."
    )

    print("\nAttack Question:")
    print(attack_question)

    print(
        "\n[1] Retrieving knowledge base..."
    )

    # Intentionally retrieve the malicious document.
    malicious_result = research_tool(
        "research assistants"
    )

    print("\nRetrieved Data:")
    print(malicious_result)

    print(
        "\n[2] Sending retrieved data to "
        "the security layer..."
    )

    final_response = generate_final_answer(
        attack_question,
        "research_tool",
        malicious_result
    )

    print("\n[3] Security Result:")

    print(
        json.dumps(
            final_response,
            indent=2
        )
    )


# ============================================================
# INTERACTIVE CLI
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # RUN INDIRECT INJECTION SECURITY TEST
    # --------------------------------------------------------

    test_indirect_prompt_injection()

    # --------------------------------------------------------
    # START INTERACTIVE ASSISTANT
    # --------------------------------------------------------

    print("=" * 60)
    print("DAY 29-30 SECURE RESEARCH ASSISTANT")
    print("=" * 60)

    print("\nModel:", MODEL)

    print("\nType 'exit' to quit.")

    while True:

        question = input(
            "\nResearch Question: "
        ).strip()

        if question.lower() == "exit":

            print("\nGoodbye!")

            break

        if not question:

            print(
                "Please enter a question."
            )

            continue

        try:

            research_agent(question)

        except Exception as error:

            print("\nAgent Error:")

            print(error)