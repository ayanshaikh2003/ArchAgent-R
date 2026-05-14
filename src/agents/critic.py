from src.services.ai_service import ask_ai

def critic(result):
    prompt = f"Review this solution and suggest improvements: {result}"
    return ask_ai(prompt)