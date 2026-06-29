from utils.gemini_client import model


def financial_analysis(startup_idea):
    """
    Generates a financial plan for a startup idea.
    """

    prompt = f"""
    You are an experienced startup financial consultant.

    Analyze the following startup idea:

    Startup Idea:
    {startup_idea}

    Generate a professional financial plan.

    Include:

    1. Estimated Initial Investment
    2. Expected Revenue Streams
    3. Monthly Operating Expenses
    4. Revenue Projection (Year 1)
    5. Break-even Analysis
    6. Funding Requirement
    7. Financial Risks
    8. Suggestions for Improving Profitability

    Format using markdown headings and bullet points.
    """

    response = model.generate_content(prompt)

    return response.text