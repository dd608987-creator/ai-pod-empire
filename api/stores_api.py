from fastapi import APIRouter
from agents.store_manager import StoreManager

router = APIRouter(prefix="/stores")

@router.post("/publish")
def publish(product: str, platform: str):
    return StoreManager().publish(product, platform)
