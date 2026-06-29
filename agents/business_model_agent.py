from utils.gemini_client import model


def business_model_analysis(startup_idea):

    prompt = f"""
    You are an expert startup strategist.

    Create a Business Model Canvas for:

    {startup_idea}

    Provide:

    1. Value Proposition
    2. Customer Segments
    3. Revenue Streams
    4. Key Activities
    5. Key Resources
    6. Key Partners
    7. Cost Structure

    Format using markdown headings and bullet points.
    """

    response = model.generate_content(prompt)

    return response.text