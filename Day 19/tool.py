from datetime import datetime

def calculator(expression):
    """
    Evaluates a mathematical expression.
    """
    try:
        return eval(expression)
    except Exception:
        return "Invalid Expression"


def get_current_time():
    """
    Returns the current system time.
    """
    return datetime.now().strftime("%I:%M:%S %p")