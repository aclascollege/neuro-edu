"""
ACLAS Neuro-Edu — FastAPI Application
All endpoints are real: they hit live agent MLPs, real training loops, and live metrics.
"""
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Optional
import uvicorn

from core.engine import UltimateClassroom

app = FastAPI(
    title="ACLAS Neuro-Edu API",
    description="Cognitive simulation engine with real backprop agents",
    version="3.0.0",
)

classroom = UltimateClassroom()
classroom.setup(20)


# --- Request Models ---
class InstructionReq(BaseModel):
    text: str
    complexity: float = 0.5
    skills_req: Optional[Dict[str, float]] = None


class SetupReq(BaseModel):
    agent_count: int = 20


# --- Endpoints ---

@app.get("/api/status")
async def status():
    """Live status of all agents."""
    return {
        "tick": classroom.tick,
        "agent_count": len(classroom.agents),
        "dataset_size": len(classroom._dataset),
        "agents": [
            {
                "id": a.id,
                "name": a.name,
                "profile": a.profile,
                "mood": a.current_mood,
                "attention": a.attention,
                "fatigue": a.fatigue,
                "prob": a.last_prob,
                "thought": a.last_thought,
                "skills": a.skill_matrix.to_dict(),
                "knowledge_count": len(a.knowledge_pool),
                "brain_sig": round(a.brain.get_weights_signature(), 5),
                "loss_curve": a.brain.get_loss_curve(20),
            }
            for a in classroom.agents
        ],
    }


@app.post("/api/teach")
async def teach(req: InstructionReq):
    """
    Broadcast an instruction to all agents.
    Each agent runs its MLP for inference, then the social learning bus fires.
    """
    skills = req.skills_req or {"logic": 0.5, "language": 0.5}
    result = classroom.broadcast(req.text, req.complexity, skills)
    return result


@app.post("/api/train")
async def train():
    """
    Run federated training across all agent brains.
    Each agent performs real backpropagation on the shared dataset.
    Returns epoch losses — you will see them decrease.
    """
    if not classroom._dataset:
        raise HTTPException(status_code=400, detail="No training data loaded")
    result = classroom.run_training(epochs=5)
    return result


@app.get("/api/metrics")
async def metrics():
    """
    Full evaluation report:
    GPA, CAS Score, Retention Rate, Shannon Diversity Index, Dropout Risk.
    """
    return classroom.get_metrics()


@app.get("/api/graph")
async def knowledge_graph():
    """Export the live knowledge graph as D3.js-compatible JSON."""
    return classroom.get_graph()


@app.post("/api/reset")
async def reset(req: SetupReq = SetupReq()):
    """Reset the simulation environment."""
    classroom.setup(req.agent_count)
    return {"status": "reset", "agents": req.agent_count}


@app.get("/api/architecture")
async def architecture():
    """Return the neural architecture of agent brains."""
    if not classroom.agents:
        return {}
    return classroom.agents[0].brain.get_architecture_summary()


@app.get("/api/dataset")
async def dataset_info():
    return {
        "size": len(classroom._dataset),
        "sample": classroom._dataset[:3] if classroom._dataset else [],
    }


# Serve frontend
app.mount("/", StaticFiles(directory="docs", html=True), name="web")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
