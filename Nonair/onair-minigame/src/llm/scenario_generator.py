import os
import json
import random
import google.generativeai as genai
from ..utils.prompts import SYSTEM_PROMPTS, Persona

# Mock data for fallback
MOCK_SCENARIOS = [
    {"caller_name": "Unknown Number", "situation": "It's an unknown number, but the area code looks familiar. Maybe it's that delivery you were expecting?"},
    {"caller_name": "Best Friend", "situation": "Your best friend is calling. They usually text, so it might be something exciting!"},
    {"caller_name": " Spam Risk", "situation": "The screen says 'Spam Risk'. Probably just another robocall offering infinite insurance."},
    {"caller_name": "Mom", "situation": "Mom is calling. It's sunday afternoon, so she probably just wants to chat about the cat."},
]

async def generate_scenario():
    """
    Generates a phone call scenario.
    Tries to use Gemini API first. If fails or no key, returns a mock scenario.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Warning: GEMINI_API_KEY not found. Using mock mode.")
        return get_mock_scenario()

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        response = model.generate_content(SYSTEM_PROMPTS[Persona.SCENARIO_CREATOR])
        
        # Simple cleanup to ensure JSON parsing
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        scenario_data = json.loads(cleaned_text)
        
        return scenario_data

    except Exception as e:
        print(f"LLM Generation Error: {e}. Falling back to mock.")
        return get_mock_scenario()

def get_mock_scenario():
    return random.choice(MOCK_SCENARIOS)
