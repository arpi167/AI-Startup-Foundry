import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    """
    Analyze this startup idea:

    Smart E-Waste Recycling Platform

    Provide:
    1. Problem Statement
    2. Target Audience
    3. Key Opportunity
    4. Opportunity Score (1-10)
    """
)

print(response.text)