from pydantic import BaseModel
from typing import Optional

# Observation: what agent sees
class Observation(BaseModel):
    email: str
    last_action: Optional[str] = None


# Action: what agent does
class Action(BaseModel):
    classification: str   # spam / urgent / normal
    priority: int         # 1–3
    reply: str


# Reward model
class Reward(BaseModel):
    score: float
