from utils.gemini_client import model


def competitor_analysis(startup_idea):

    prompt = f"""
    You are an expert startup competitor analyst.

    Analyze competitors for:

    {startup_idea}

    Return:

    1. Top Competitors
    2. Competitor Strengths
    3. Competitor Weaknesses
    4. Market Gaps
    5. SWOT Analysis

    Format using markdown headings and bullet points.
    """

    response = model.generate_content(prompt)

    return response.text