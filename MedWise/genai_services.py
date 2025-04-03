import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GENAI_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def genai_response(prompt):
    response = model.generate_content(prompt)
    return response.text
