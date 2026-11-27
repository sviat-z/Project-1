import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()  # читає ключ з файлу .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = """You are a nutrition assistant.
Estimate the nutrition for this meal: "{food}"
Return ONLY JSON with these keys (numbers, no units):
{{"calories": int, "protein": float, "carbs": float, "fat": float}}"""

def estimate_nutrition(food_text):
    """Повертає словник з калоріями і макросами, або None при помилці."""
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=PROMPT.format(food=food_text),
            config={"response_mime_type": "application/json"},
        )
        return json.loads(response.text)
    except Exception as e:
        print("AI error:", e)
        return None

# Швидкий тест: python3 ai.py
if __name__ == "__main__":
    print(estimate_nutrition("2 eggs and toast"))