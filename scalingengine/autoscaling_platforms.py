import random
import statistics

class PlatformAutoScaler:
    def __init__(self, logger=None):
        self.logger = logger

        self.platforms = [
            "TikTok",
            "Instagram",
            "YouTube Shorts",
            "Facebook Reels"
        ]

    def score_platform(self, platform):
        """
        Generates a performance score for each platform.
        """

        return random.randint(40, 100)

    def analyze(self, marketing_results):
        """
        Analyzes platform performance based on marketing output.
        """

        platform_scores = []

        for result in marketing_results:
            score = self.score_platform(result["platform"])
            platform_scores.append({
                "platform": result["platform"],
                "score": score
            })

        avg_score = statistics.mean([p["score"] for p in platform_scores])

        # Determine scaling strategy
        best_platform = max(platform_scores, key=lambda x: x["score"])
        worst_platform = min(platform_scores, key=lambda x: x["score"])

        scaling_strategy = {
            "scale_up": best_platform["platform"],
            "scale_down": worst_platform["platform"],
            "recommended_posting_frequency": random.choice([
                "3 posts/day",
                "5 posts/day",
                "1 post/day",
                "2 posts/day"
            ])
        }

        return {
            "status": "platform_scaling_complete",
            "platform_scores": platform_scores,
            "average_score": avg_score,
            "strategy": scaling_strategy
        }
