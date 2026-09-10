MAX_STEPS = 5


def validate_input(user_input: str):
    """
    Basic guardrails for user input.
    """

    if len(user_input.strip()) == 0:
        return False, "Input cannot be empty."

    if len(user_input) > 500:
        return False, "Input is too long."

    return True, ""