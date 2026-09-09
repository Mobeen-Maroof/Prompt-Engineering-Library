from ollama import chat


def research_agent(topic: str) -> str:
    """Researches the given topic using the AI model."""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Research Agent. "
                    "Provide concise research notes about the user's topic."
                ),
            },
            {
                "role": "user",
                "content": topic,
            },
        ],
    )

    return response.message.content


def writer_agent(topic: str, research_notes: str) -> str:
    """Writes a final response based on the research notes."""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Writer Agent. "
                    "Use the provided research notes to create a clear, "
                    "well-structured response for the user."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n\n"
                    f"Research Notes:\n{research_notes}\n\n"
                    "Write the final answer."
                ),
            },
        ],
    )

    return response.message.content
