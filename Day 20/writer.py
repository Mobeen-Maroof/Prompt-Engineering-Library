def write_article(research):

    if "Error" in research:
        return research["Error"]

    article = f"""
Topic: {research['Topic']}

Definition:
{research['Definition']}

Applications:
"""

    for app in research["Applications"]:
        article += f"- {app}\n"

    article += "\nConclusion:\nThis information was prepared by the Writer Agent."

    return article