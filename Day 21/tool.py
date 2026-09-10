from datetime import datetime


def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def current_time() -> str:
    """Return the current system time."""
    return datetime.now().strftime("%I:%M:%S %p")
