from utils.gemini_client import model


def validate_startup_idea(startup_idea):
    """
    Validates a startup idea and returns a structured analysis.
    """

    prompt = f"""
    You are an experienced startup mentor.

    Analyze the following startup idea:

    Startup Idea:
    {startup_idea}

    Generate a detailed analysis containing:

    1. Problem Statement
    2. Target Audience
    3. Key Opportunity
    4. Opportunity Score (1-10)
    5. Justification for the Score

    Format the response using proper markdown headings and bullet points.
    """

    response = model.generate_content(prompt)

    return response.text