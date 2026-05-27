from fastapi import APIRouter
from unified_brain import UnifiedBrain

router = APIRouter()

# Fake instance (replace with your real instance)
brain = None

@router.get("/dashboard/metrics")
def get_metrics():
    return {
        "status": "ok",
        "brain_state": "running",
        "platform_scaling": {
            "scale_up": "TikTok",
            "scale_down": "Facebook Reels",
            "recommended_frequency": "3 posts/day"
        },
        "latest_video": {
            "status": "published",
            "platform": "TikTok"
        }
    }

@router.get("/dashboard/analytics")
def get_analytics():
    return {
        "video_performance": [
            {"platform": "TikTok", "score": 92},
            {"platform": "Instagram", "score": 78},
            {"platform": "YouTube Shorts", "score": 85}
        ],
        "market_trend": "Arabic Calligraphy",
        "design_quality": 0.88
    }
