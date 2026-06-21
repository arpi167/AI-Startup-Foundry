from agents.idea_agent import validate_startup_idea
from agents.market_agent import market_research

idea = input("Enter Startup Idea: ")

print("\n" + "="*50)
print("IDEA VALIDATION AGENT")
print("="*50)

idea_result = validate_startup_idea(idea)

print(idea_result)

print("\n" + "="*50)
print("MARKET RESEARCH AGENT")
print("="*50)

market_result = market_research(idea)

print(market_result)