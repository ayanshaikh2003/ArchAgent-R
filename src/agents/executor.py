from src.services.ai_service import ask_ai

def executor(plan):
    prompt = f"Explain how to implement this system step by step: {plan}"
    return ask_ai(prompt)