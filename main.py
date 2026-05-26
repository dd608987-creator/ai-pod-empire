from fastapi import FastAPI
from api.empire_api import router as empire_router
from api.agents_api import router as agents_router
from api.stores_api import router as stores_router
from api.marketplace_api import router as marketplace_router

app = FastAPI(
    title="AI POD Empire",
    description="Autonomous multi-agent POD empire powered by Unified Brain",
    version="1.0.0"
)

# Routers
app.include_router(empire_router)
app.include_router(agents_router)
app.include_router(stores_router)
app.include_router(marketplace_router)

@app.get("/")
def home():
    return {
        "status": "AI POD Empire is running",
        "message": "Welcome to the autonomous POD empire"
    }
