from fastapi import APIRouter
from agents.trend_agent import TrendAgent
from agents.design_agent import DesignAgent
from agents.mockup_agent import MockupAgent
from agents.collection_agent import CollectionAgent

router = APIRouter(prefix="/agents")

@router.post("/trend")
def trend(market: str):
    return TrendAgent().generate(market)

@router.post("/design")
def design(niche: str):
    return DesignAgent().generate(niche)

@router.post("/mockup")
def mockup(design_url: str):
    return MockupAgent().generate(design_url)

@router.post("/collections")
def collections(niche: str):
    return CollectionAgent().generate(niche)
