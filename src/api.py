from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.agents.planner import planner
from src.agents.executor import executor
from src.agents.critic import critic
from src.agents.tech_stack import tech_stack
from src.agents.diagram_agent import generate_diagram

app = FastAPI()

# Enable frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def home():
    return {"message": "ArchAgent-R API is running"}

# Main AI processing route
@app.get("/process")
def process(input_text: str):

    # Agent 1 → Planner
    plan = planner(input_text)

    # Agent 2 → Tech Stack Recommendation
    stack = tech_stack(input_text)

    # Agent 3 → Diagram Generator
    diagram = generate_diagram(input_text)

    # Agent 4 → Execution Steps
    result = executor(plan)

    # Agent 5 → Review / Critic
    review = critic(result)

    return {
        "input": input_text,
        "plan": plan,
        "tech_stack": stack,
        "diagram": diagram,
        "execution": result,
        "review": review
    }