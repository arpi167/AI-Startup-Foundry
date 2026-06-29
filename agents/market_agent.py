from utils.gemini_client import model

def market_research(startup_idea):

    prompt = f"""
    You are a market research expert.

    Analyze the following startup idea:

    {startup_idea}

    Provide:

    1. Industry Overview
    2. Market Trends
    3. Customer Segments
    4. Growth Potential
    5. Key Opportunities

    Keep the response structured and practical.
    """

    response = model.generate_content(prompt)

    return response.text