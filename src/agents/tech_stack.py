from src.services.ai_service import ask_ai

def tech_stack(requirement):

    prompt = f"""
    Suggest the best technology stack for this system:

    {requirement}

    Include:
    - Frontend
    - Backend
    - Database
    - Authentication
    - Cloud/Deployment

    Keep it clear and professional.
    """

    return ask_ai(prompt)