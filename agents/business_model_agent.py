import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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