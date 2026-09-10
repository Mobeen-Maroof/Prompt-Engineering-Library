from ollama import chat


def research_agent(topic):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content":
                "You are a Research Agent. Give short research notes."
            },
            {
                "role": "user",
                "content": topic
            }
        ]
    )

    return response.message.content


def writer_agent(topic, notes):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content":
                "You are a Writer Agent. Use the research notes to write the final answer."
            },
            {
                "role": "user",
                "content":
                f"Topic: {topic}\n\nResearch:\n{notes}"
            }
        ]
    )

    return response.message.content
