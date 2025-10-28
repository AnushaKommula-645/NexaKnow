import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """
    Extracts readable text from a webpage URL.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip()) > 40]
        text = ' '.join(paragraphs)
        return text[:4000] if len(text) > 4000 else text
    except Exception as e:
        return f"Error extracting text: {e}"
