from agents import research_agent, writer_agent

print("=" * 60)
print("         Day 20 - Multi-Agent System")
print("=" * 60)

while True:

    topic = input("\nEnter a topic (or type 'exit' to quit): ")

    if topic.lower() == "exit":
        print("\nGoodbye!")
        break

    print("\n🔍 Research Agent is working...")
    research = research_agent(topic)

    print("\n==============================")
    print("Research Notes")
    print("==============================")
    print(research)

    print("\n✍️ Writer Agent is writing...")

    final_answer = writer_agent(topic, research)

    print("\n==============================")
    print("Final Answer")
    print("==============================")
    print(final_answer)
