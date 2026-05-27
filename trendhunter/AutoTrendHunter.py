import random
import datetime


class AutoTrendHunter:
    def __init__(self, logger=None):
        self.logger = logger

        self.countries = ["DZ", "MA", "FR", "ES", "CA", "US", "DE", "GB"]
        self.platforms = ["TikTok", "Instagram", "YouTube Shorts", "X"]

    def fetch_raw_trends(self, market="global"):
        """
        هنا لاحقًا تربط:
        - TikTok Trending API
        - Google Trends
        - Twitter/X Trends
        - Etsy / Redbubble / Amazon POD
        الآن نرجع بيانات وهمية منظمة بنفس الشكل.
        """

        trends = []

        for _ in range(10):
            trends.append({
                "keyword": random.choice([
                    "dz vs ma",
                    "algeria vs morocco",
                    "kabyle aesthetic",
                    "north africa streetwear",
                    "arabic calligraphy hoodie",
                    "maghreb football meme",
                    "berber symbol design",
                    "ramadan vibes 2026",
                    "eid outfits 2026",
                    "world cup nostalgia"
                ]),
                "country": random.choice(self.countries),
                "platform": random.choice(self.platforms),
                "score": random.randint(60, 100),
                "velocity": random.uniform(0.4, 1.0),  # سرعة صعود الترند
                "timestamp": datetime.datetime.utcnow().isoformat()
            })

        if self.logger:
            self.logger.info("AutoTrendHunter: fetched raw trends.")

        return trends

    def rank_trends(self, trends):
        """
        ترتيب الترندات حسب:
        - score
        - velocity
        - توافقها مع POD
        """

        ranked = sorted(
            trends,
            key=lambda t: (t["score"] * 0.7 + t["velocity"] * 30),
            reverse=True
        )

        return ranked

    def filter_for_pod(self, ranked_trends):
        """
        اختيار الترندات المناسبة للطباعة عند الطلب:
        - فيها هوية
        - فيها انتماء
        - فيها meme / rivalry
        """

        pod_trends = []

        for t in ranked_trends:
            kw = t["keyword"].lower()
            if any(x in kw for x in ["vs", "hoodie", "streetwear", "aesthetic", "design", "vibes", "outfits", "symbol"]):
                pod_trends.append(t)

        return pod_trends[:5]

    def hunt(self, market="global"):
        """
        Full pipeline:
        - fetch_raw_trends
        - rank_trends
        - filter_for_pod
        """

        raw = self.fetch_raw_trends(market=market)
        ranked = self.rank_trends(raw)
        pod_ready = self.filter_for_pod(ranked)

        result = {
            "status": "trend_hunt_complete",
            "market": market,
            "raw_trends_count": len(raw),
            "top_trends": ranked[:10],
            "pod_trends": pod_ready
        }

        if self.logger:
            self.logger.info("AutoTrendHunter: hunt completed.")

        return result
