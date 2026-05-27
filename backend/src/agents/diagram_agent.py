from src.services.ai_service import ask_ai

def generate_diagram(input_text):
    prompt = f"""
Generate ONLY valid Mermaid.js code for a software architecture diagram.

System:
{input_text}

Strict rules:
- Start with exactly: graph TD
- Do not use markdown
- Do not use ```mermaid
- Do not use explanations
- Do not use slash symbols /
- Do not use parentheses ()
- Do not use colons :
- Keep node labels simple
- Use only letters, numbers, and spaces inside brackets

Return a diagram similar to:

graph TD
A[User] --> B[Web Frontend]
B --> C[Load Balancer]
C --> D[API Gateway]
D --> E[Authentication Service]
D --> F[Product Service]
D --> G[Order Service]
F --> H[Redis Cache]
F --> I[Database]
G --> J[Payment Service]
J --> K[External Payment Gateway]
G --> I
"""

    diagram = ask_ai(prompt)

    diagram = diagram.replace("```mermaid", "")
    diagram = diagram.replace("```", "")
    diagram = diagram.replace("/", " ")
    diagram = diagram.replace(":", " ")
    diagram = diagram.replace("(", "")
    diagram = diagram.replace(")", "")
    diagram = diagram.strip()

    if not diagram.startswith("graph"):
        diagram = """
graph TD
A[User] --> B[Web Frontend]
B --> C[Load Balancer]
C --> D[API Gateway]
D --> E[Authentication Service]
D --> F[Product Service]
D --> G[Order Service]
F --> H[Redis Cache]
F --> I[Database]
G --> J[Payment Service]
J --> K[External Payment Gateway]
G --> I
"""

    return diagram