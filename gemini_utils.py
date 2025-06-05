import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def ask_gemini(question, context):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"Context:\n{context}\n\nQuestion:\n{question}")
    return response.text


# $env:GOOGLE_API_KEY="AIzaSyBEmgn35jP1g62GVSfOmhfHBOMki4snsaY"
# python -m streamlit run app.py
