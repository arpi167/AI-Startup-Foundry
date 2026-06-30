from utils.gemini_client import model


def generate_pitch_deck(startup_idea):
    """
    Generates an investor-ready pitch deck outline.
    """

    prompt = f"""
    You are an experienced startup founder and venture capitalist.

    Create a professional investor pitch deck for the following startup.

    Startup Idea:
    {startup_idea}

    Generate the following slides:

    1. Startup Name & Vision
    2. Problem Statement
    3. Solution
    4. Market Opportunity
    5. Business Model
    6. Competitive Advantage
    7. Financial Highlights
    8. Go-to-Market Strategy
    9. Funding Requirement
    10. Future Roadmap

    Format the output using markdown headings and bullet points.
    """

    response = model.generate_content(prompt)

    return response.text