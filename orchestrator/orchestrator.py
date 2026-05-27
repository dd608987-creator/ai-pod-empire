from trendhunter.AutoTrendHunter import AutoTrendHunter


class Orchestrator:
    def __init__(self, agents, memory, autoscaler, autolearn, autorevenue, autodesevo, logger=None):
        self.agents = agents
        self.memory = memory
        self.autoscaler = autoscaler
        self.autolearn = autolearn
        self.autorevenue = autorevenue
        self.autodesevo = autodesevo
        self.logger = logger

        # Trend Hunter Engine
        self.trend_hunter = AutoTrendHunter(logger=logger)

    def run_cycle(self, market):
        if self.logger:
            self.logger.info("Orchestrator: running cycle.")

        # 1) Hunt trends
        trend_data = self.trend_hunter.hunt(market=market)
        pod_trends = trend_data.get("pod_trends", [])

        # 2) Generate designs from trends
        designs = []
        if "design" in self.agents:
            for t in pod_trends:
                trend_kw = t["keyword"]
                design = self.agents["design"].generate_design_from_trend(trend_kw)
                designs.append(design)

        # 3) Create collections (optional placeholder)
        collections = [
            {"collection_id": "col_auto_001", "items": designs}
        ]

        # 4) Save to memory
        self.memory.save({
            "latest_trends": pod_trends,
            "generated_designs": designs,
            "market": market
        })

        return {
            "status": "orchestrator_cycle_complete",
            "market": market,
            "trends": trend_data,
            "designs": designs,
            "collections": collections
        }
