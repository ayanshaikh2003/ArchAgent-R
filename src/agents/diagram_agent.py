from src.services.ai_service import ask_ai

def generate_diagram(input_text):
    prompt = f"""
You are a senior software architect.

Generate a DETAILED Mermaid.js architecture diagram for the following software system:

System requirement:
{input_text}

Your diagram must include:
- User / Client
- Web or Mobile Frontend
- Load Balancer
- API Gateway
- Authentication Service
- Main Business Services
- Database
- Cache layer such as Redis
- External services if relevant
- Cloud / Deployment layer if relevant

Rules:
- Return ONLY valid Mermaid code
- Do NOT include explanation
- Do NOT include markdown fences
- Do NOT write ```mermaid
- Start directly with: graph TD
- Use simple node names
- Avoid special symbols like (), /, &, :
- Use square brackets only for node labels
- Keep the diagram readable and professional

Example format:
graph TD
A[User] --> B[Frontend]
B --> C[Load Balancer]
C --> D[API Gateway]
D --> E[Auth Service]
D --> F[Product Service]
D --> G[Order Service]
F --> H[Redis Cache]
F --> I[Database]
G --> I
G --> J[Payment Gateway]
"""

    diagram = ask_ai(prompt)

    # Clean common unwanted formatting from AI output
    diagram = diagram.replace("```mermaid", "")
    diagram = diagram.replace("```", "")
    diagram = diagram.strip()

    # Safety fallback if AI does not return Mermaid
    if not diagram.startswith("graph"):
        diagram = f"""
graph TD
A[User] --> B[Frontend]
B --> C[Load Balancer]
C --> D[API Gateway]
D --> E[Authentication Service]
D --> F[Core Business Service]
F --> G[Redis Cache]
F --> H[Database]
F --> I[External Service]
"""

    return diagram