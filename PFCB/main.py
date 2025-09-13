import os
import google.generativeai as genai

api_key = os.getenv("Gemini_API_KEY")
genai.configure(api_key=api_key)
gemini_client = genai.GenerativeModel('gemini-pro')