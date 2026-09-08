from datetime import datetime

def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression: Mathematical expression such as "25+8"

    Returns:
        Result of the calculation.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def current_time() -> str:
    """
    Return the current system time.

    Returns:
        Current local time.
    """
    return datetime.now().strftime("%I:%M:%S %p")
