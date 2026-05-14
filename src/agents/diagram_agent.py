from src.services.ai_service import ask_ai

def generate_diagram(input_text):

    prompt = f"""
Generate ONLY a valid Mermaid diagram.

Rules:
- Return ONLY Mermaid code
- No explanation
- No markdown
- No ```mermaid
- Start directly with graph LR
- Keep syntax simple

System:
{input_text}

Example:
graph LR
A[User] --> B[Frontend]
B --> C[Backend]
C --> D[Database]
"""

    return ask_ai(prompt)