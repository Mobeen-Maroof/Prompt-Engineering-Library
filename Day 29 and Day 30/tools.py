import ast
import operator
import os
import re


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCUMENTS_PATH = os.path.join(BASE_DIR, "documents.txt")


# ============================================================
# RESEARCH TOOL
# ============================================================

def load_documents(filename=None):
    """
    Load documents from the local knowledge base.

    The default path always points to documents.txt
    inside the main project folder, regardless of the
    current working directory.
    """

    if filename is None:
        filename = DOCUMENTS_PATH
    elif not os.path.isabs(filename):
        filename = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Knowledge base not found: {filename}"
        )

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # Split documents using headings such as:
    # [Document 1 - AI]
    # [Document 2 - Machine Learning]
    raw_documents = re.split(
        r"\n(?=\[Document\s+\d+)",
        content.strip()
    )

    documents = []

    for document in raw_documents:
        document = document.strip()

        if document:
            documents.append(document)

    return documents


def research_tool(question, filename=None):
    """
    Search the local knowledge base for information relevant
    to the user's research question.
    """

    documents = load_documents(filename)

    question_words = {
        word.lower()
        for word in re.findall(
            r"\b[a-zA-Z]{3,}\b",
            question
        )
    }

    scored_documents = []

    for document in documents:

        document_words = {
            word.lower()
            for word in re.findall(
                r"\b[a-zA-Z]{3,}\b",
                document
            )
        }

        score = len(
            question_words.intersection(document_words)
        )

        scored_documents.append(
            (score, document)
        )

    # Highest relevance score first
    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    relevant_documents = [
        document
        for score, document in scored_documents
        if score > 0
    ][:3]

    if not relevant_documents:
        return (
            "No relevant information was found in the "
            "approved knowledge base."
        )

    return "\n\n".join(
        "UNTRUSTED RETRIEVED DATA:\n" + document
        for document in relevant_documents
    )


# ============================================================
# SAFE CALCULATOR
# ============================================================

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_calculate(expression):
    """
    Safely evaluate basic mathematical expressions.

    This function does NOT use eval().
    """

    try:

        # Limit extremely large expressions
        if len(expression) > 200:
            return "Error: expression is too long."

        tree = ast.parse(
            expression,
            mode="eval"
        )

        return evaluate_node(tree.body)

    except ZeroDivisionError:
        return (
            "Error: division by zero is not allowed."
        )

    except Exception:
        return (
            "Error: Only basic mathematical expressions "
            "are allowed."
        )


def evaluate_node(node):
    """
    Recursively evaluate an approved mathematical AST.
    """

    # Numbers only
    if isinstance(node, ast.Constant):

        if isinstance(
            node.value,
            (int, float)
        ) and not isinstance(
            node.value,
            bool
        ):
            return node.value

        raise ValueError(
            "Only numbers are allowed."
        )

    # Unary operations such as -5 and +5
    if isinstance(node, ast.UnaryOp):

        operator_function = ALLOWED_OPERATORS.get(
            type(node.op)
        )

        if operator_function is None:
            raise ValueError(
                "Unsupported operator."
            )

        return operator_function(
            evaluate_node(node.operand)
        )

    # Binary operations such as 25 + 8
    if isinstance(node, ast.BinOp):

        operator_function = ALLOWED_OPERATORS.get(
            type(node.op)
        )

        if operator_function is None:
            raise ValueError(
                "Unsupported operator."
            )

        left = evaluate_node(
            node.left
        )

        right = evaluate_node(
            node.right
        )

        # Prevent unreasonable exponentiation
        if isinstance(node.op, ast.Pow):

            if abs(right) > 100:
                raise ValueError(
                    "Exponent is too large."
                )

        return operator_function(
            left,
            right
        )

    raise ValueError(
        "Unsupported expression."
    )


def calculator_tool(expression):
    """
    Public calculator tool used by the AI agent.
    """

    result = safe_calculate(
        expression
    )

    return str(result)


# ============================================================
# TOOL REGISTRY
# ============================================================

AVAILABLE_TOOLS = {

    "research_tool": research_tool,

    "calculator_tool": calculator_tool,

}


def get_available_tools():
    """
    Return the list of tools available to the AI agent.
    """

    return {

        "research_tool": {

            "description": (
                "Search the approved research "
                "knowledge base for information "
                "relevant to a question."
            ),

            "parameters": {
                "question": "string"
            },

        },

        "calculator_tool": {

            "description": (
                "Perform safe basic mathematical "
                "calculations. Supports arithmetic "
                "operations only."
            ),

            "parameters": {
                "expression": "string"
            },

        },

    }


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("TOOL TESTING")
    print("=" * 60)

    print("\nKnowledge Base:")
    print(DOCUMENTS_PATH)

    print("\n1. Research Tool Test")
    print("-" * 60)

    research_result = research_tool(
        "What is Retrieval-Augmented Generation?"
    )

    print(research_result)

    print("\n2. Calculator Test")
    print("-" * 60)

    print(
        "25 + 8 =",
        calculator_tool("25 + 8")
    )

    print(
        "100 / 4 =",
        calculator_tool("100 / 4")
    )

    print(
        "10 * 5 =",
        calculator_tool("10 * 5")
    )

    print("\n3. Division by Zero Test")
    print("-" * 60)

    print(
        calculator_tool("25 / 0")
    )

    print("\n4. Security Test")
    print("-" * 60)

    print(
        calculator_tool(
            "__import__('os').system('dir')"
        )
    )

    print("\n5. Available Tools")
    print("-" * 60)

    for name, information in get_available_tools().items():

        print(f"{name}:")

        print(information)