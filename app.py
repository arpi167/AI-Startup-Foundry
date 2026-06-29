from agents.idea_agent import validate_startup_idea
from agents.market_agent import market_research
from agents.competitor_agent import competitor_analysis
from agents.business_model_agent import business_model_analysis
from agents.financial_agent import financial_analysis

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

print("\n" + "="*50)
print("COMPETITOR ANALYSIS AGENT")
print("="*50)

competitor_result = competitor_analysis(idea)

print(competitor_result)

print("\n" + "="*50)
print("BUSINESS MODEL AGENT")
print("="*50)

business_result = business_model_analysis(idea)

print(business_result)

print("\n" + "="*50)
print("FINANCIAL PLANNING AGENT")
print("="*50)

financial_result = financial_analysis(idea)

print(financial_result)