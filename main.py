import os
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from ai.openrouter import OpenRouter
from dotenv import load_dotenv
from auth.dependencies import get_user_identifier
from auth.throttling import apply_rate_limit
import requests.exceptions


load_dotenv()

# --- App Initialization ---
app = FastAPI()


# --- AI Configuration ---
def load_system_prompt():
    try:
        with open("prompts/system_prompt.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


system_prompt = load_system_prompt()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable not set.")

ai_platform = OpenRouter(api_key=openrouter_api_key, system_prompt=system_prompt)


# --- Pydantic Models ---
class ChatRequest(BaseModel):
    prompt: str
    model: str = None  # Optional model parameter


class ChatResponse(BaseModel):
    response: str


# --- API Endpoints ---
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
    apply_rate_limit(user_id)

    # Set model if provided in request
    if request.model:
        ai_platform.model = request.model

    try:
        response_text = ai_platform.chat(request.prompt)
        return ChatResponse(response=response_text)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401 or e.response.status_code == 403:
            raise HTTPException(
                status_code=403,
                detail="API key permission denied. Please check your API key and permissions.",
            )
        else:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"OpenRouter API error: {str(e)}",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/")
async def root():
    return {"message": "API is running"}
