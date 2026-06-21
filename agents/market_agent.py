import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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