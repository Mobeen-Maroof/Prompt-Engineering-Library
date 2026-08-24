from researcher import research
from writer import write_article

topic = "Artificial Intelligence"

print("="*60)
print("Multi-Agent System Demo")
print("="*60)

print("\nAgent 1 : Researcher")

research_data = research(topic)

print(research_data)

print("\nPassing information to Writer Agent...\n")

print("Agent 2 : Writer\n")

article = write_article(research_data)

print(article)