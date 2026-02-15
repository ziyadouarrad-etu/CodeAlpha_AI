import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

class GeminiTranslator:
    def __init__(self):
        # Configure the API key from .env
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')

    def translate(self, text, target_lang):
        # Prompt for Detection + Translation
        prompt = f"""
        You are a professional multilingual translator. 
        1. Identify the language of the provided text.
        2. Translate the text into {target_lang}.
        
        Output strictly in this JSON format:
        {{
            "detected_language": "NAME_OF_DETECTED_LANGUAGE",
            "detected_language_code": "LANGUAGE_CODE", # e.g., 'en' for English
            "original_text": "{text}",
            "target_language": "{target_lang}",
            "target_language_code": "TARGET_LANGUAGE_CODE" # e.g., 'fr' for French
            "translated_text": "YOUR_TRANSLATION_HERE",
        }}
        """
        try:
            response = self.model.generate_content(prompt)
            # Cleaning potential markdown code blocks from the response
            clean_json = response.text.strip('`json\n ')
            return json.loads(clean_json)
        except Exception as e:
            return {"error": str(e)}
    
    def get_mock_translation(self, text, target_lang):
        """Returns a fake response to save API quota during UI testing."""
        return {
            "detected_language": "English",
            "detected_language_code": "en",
            "original_text": text,
            "translated_text": "Bonjour le monde",  # "Hello World" in French
            "target_language": target_lang,
            "target_language_code": "fr" # Defaulting to French for gTTS test
        }