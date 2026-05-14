from src.services.ai_service import ask_ai

def generate_diagram(requirement):

    prompt = f"""
    Generate a Mermaid.js system architecture diagram
    for this software system:

    {requirement}

    Return ONLY Mermaid code.

    Example:
    graph TD
    User --> Frontend
    Frontend --> Backend
    Backend --> Database
    """

    return ask_ai(prompt)