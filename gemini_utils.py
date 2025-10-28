from google import genai
import os
from dotenv import load_dotenv

# Load your .env file (make sure it contains GEMINI_API_KEY)
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(question, context):
    """
    Sends a context and question to the Gemini model and returns the generated answer.
    """
    try:
        prompt = f"Context:\n{context}\n\nQuestion:\n{question}"
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
