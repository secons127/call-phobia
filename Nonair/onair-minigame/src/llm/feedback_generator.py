import os
import random
import google.generativeai as genai
from ..utils.prompts import SYSTEM_PROMPTS, Persona

MOCK_FEEDBACK = [
    "That's perfectly okay! You made a choice that feels right for you.",
    "Great job listening to your own needs. There's no rush to pick up every call.",
    "It takes courage to decide. You're doing great!",
    "Ignoring is a valid option. Your peace of mind matters most."
]

async def generate_feedback(scenario_context: dict, user_choice: str):
    """
    Generates comforting feedback based on the user's choice.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return {"message": random.choice(MOCK_FEEDBACK)}

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
        {SYSTEM_PROMPTS[Persona.FEEDBACK_THERAPIST]}
        
        [Scenario Info]
        Caller: {scenario_context.get('caller_name', 'Unknown')}
        Situation: {scenario_context.get('situation', 'N/A')}
        
        [User Choice]
        {user_choice}
        """
        
        response = model.generate_content(prompt)
        return {"message": response.text.strip()}

    except Exception as e:
        print(f"Feedback Gen Error: {e}")
        return {"message": random.choice(MOCK_FEEDBACK)}
