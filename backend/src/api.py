from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.agents.planner import planner
from src.agents.executor import executor
from src.agents.critic import critic
from src.agents.tech_stack import tech_stack
from src.agents.diagram_agent import generate_diagram

from src.database import init_db, create_user, login_user, save_history, get_history

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class HistoryRequest(BaseModel):
    user_id: int
    input_text: str
    modification: str = ""

@app.get("/")
def home():
    return {"message": "ArchAgent-R API is running"}

@app.post("/register")
def register(user: RegisterRequest):
    try:
        create_user(user.name, user.email, user.password)
        return {"message": "User registered successfully"}
    except Exception:
        return {"message": "User already exists or registration failed"}

@app.post("/login")
def login(user: LoginRequest):
    result = login_user(user.email, user.password)

    if result:
        user_id, name, email = result
        return {
            "message": "Login successful",
            "user": {
                "id": user_id,
                "name": name,
                "email": email
            }
        }

    return {"message": "Invalid email or password"}

@app.get("/history")
def history(user_id: int):
    rows = get_history(user_id)

    return {
        "history": [
            {
                "input_text": row[0],
                "modification": row[1],
                "created_at": row[2]
            }
            for row in rows
        ]
    }

@app.post("/save-history")
def save_user_history(item: HistoryRequest):
    save_history(item.user_id, item.input_text, item.modification)
    return {"message": "History saved"}

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