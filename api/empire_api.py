from fastapi import APIRouter
from os.empire_os import EmpireOS
from agents.trend_agent import TrendAgent
from agents.design_agent import DesignAgent
from agents.mockup_agent import MockupAgent
from agents.collection_agent import CollectionAgent

router = APIRouter(prefix="/empire")

agents = {
    "trend": TrendAgent(),
    "design": DesignAgent(),
    "mockups": MockupAgent(),
    "collections": CollectionAgent()
}

os = EmpireOS(agents=agents)

@router.post("/run")
def run_full_cycle(market: str = "US"):
    return os.run(market)

@router.post("/brain")
def brain_only(context: dict):
    return os.brain.think(context)
