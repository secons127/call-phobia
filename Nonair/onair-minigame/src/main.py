import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Import our logic (Need to ensure src package is resolvable if running from root)
# Alternatively, use relative imports if running as module
from .llm.scenario_generator import generate_scenario
from .llm.feedback_generator import generate_feedback

load_dotenv()

app = FastAPI(title="ON:AIR Mini Game API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models ---
class ScenarioResponse(BaseModel):
    caller_name: str
    situation: str

class UserPick(BaseModel):
    choice: str  # 'accept', 'wait', 'ignore'
    scenario_context: dict 

class FeedbackResponse(BaseModel):
    message: str

# --- API Endpoints ---

@app.get("/api/health")
def health_check():
    return {"status": "ok", "env": os.getenv("APP_ENV", "development")}

@app.get("/api/scenario", response_model=ScenarioResponse)
async def get_scenario():
    """Generates a new phone call scenario."""
    data = await generate_scenario()
    return data

@app.post("/api/feedback", response_model=FeedbackResponse)
async def get_feedback(pick: UserPick):
    """Generates supportive feedback based on user choice."""
    data = await generate_feedback(pick.scenario_context, pick.choice)
    return data

# Mount static files (Frontend) - This allows serving index.html directly from localhost:8000
# Ensure the directory exists relative to where uvicorn is run
# We assume running from root, so 'src/frontend'
static_dir = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="frontend")
else:
    print(f"Warning: Static directory {static_dir} not found. Frontend serving disabled.")
