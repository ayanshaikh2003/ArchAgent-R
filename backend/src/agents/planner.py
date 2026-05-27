from src.services.ai_service import ask_ai

def planner(input_text):
    prompt = f"Design a detailed software architecture for: {input_text}"
    return ask_ai(prompt)