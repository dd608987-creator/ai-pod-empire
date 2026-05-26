from fastapi import APIRouter

router = APIRouter(prefix="/marketplace")

@router.get("/agents")
def list_agents():
    return ["trend", "design", "mockups", "collections"]

@router.post("/install")
def install(agent_id: str):
    return {"status": "installed", "agent": agent_id}

@router.post("/publish")
def publish(agent_id: str):
    return {"status": "published", "agent": agent_id}
