from datetime import datetime

def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def current_time():
    return datetime.now().strftime("%I:%M:%S %p")
