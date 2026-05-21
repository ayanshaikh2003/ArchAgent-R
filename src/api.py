from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.agents.planner import planner
from src.agents.executor import executor
from src.agents.critic import critic
from src.agents.tech_stack import tech_stack
from src.agents.diagram_agent import generate_diagram

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "ArchAgent-R API is running"}

@app.get("/process")
def process(input_text: str, modification: str = ""):
    full_prompt = input_text

    if modification:
        full_prompt += f". Modification request: {modification}"

    plan = planner(full_prompt)
    stack = tech_stack(full_prompt)
    diagram = generate_diagram(full_prompt)
    result = executor(plan)
    review = critic(result)

    return {
        "input": input_text,
        "modification": modification,
        "plan": plan,
        "tech_stack": stack,
        "diagram": diagram,
        "execution": result,
        "review": review
    }