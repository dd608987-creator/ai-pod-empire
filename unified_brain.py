from orchestrator.orchestrator import Orchestrator
from reasoning.reasoning_core import ReasoningCore
from video_engine.tiktok_video_generator import TikTokVideoGenerator

from marketingengine.automarketing import AutoMarketingEngine
from analyticengine.autoanalytics import AutoAnalyticsEngine
from scalingengine.autoscaling_platforms import PlatformAutoScaler

from tokenmanager.tiktok_token_manager import TikTokTokenManager


class UnifiedBrain:
    def __init__(
        self,
        agents,
        memory,
        autoscaler,
        autolearn,
        autorevenue,
        autodesevo,
        logger=None
    ):
        self.agents = agents
        self.memory = memory
        self.autoscaler = autoscaler
        self.autolearn = autolearn
        self.autorevenue = autorevenue
        self.autodesevo = autodesevo
        self.logger = logger

        # Reasoning Engine
        self.reasoning = ReasoningCore(logger=logger)

        # Orchestrator
        self.orchestrator = Orchestrator(
            agents=agents,
            memory=memory,
            autoscaler=autoscaler,
            autolearn=autolearn,
            autorevenue=autorevenue,
            autodesevo=autodesevo,
            logger=logger
        )

        # TikTok Video Engine
        self.video_engine = TikTokVideoGenerator(logger=logger)

        # TikTok Token Manager (REAL)
        self.token_manager = TikTokTokenManager(
            client_key="YOUR_CLIENT_KEY",
            client_secret="YOUR_CLIENT_SECRET",
            refresh_token="YOUR_REFRESH_TOKEN",
            logger=logger
        )

        # Auto‑Marketing Engine (REAL TikTok Publisher)
        self.marketing = AutoMarketingEngine(
            token_manager=self.token_manager,
            logger=logger
        )

        # Auto‑Analytics Engine
        self.analytics = AutoAnalyticsEngine(logger=logger)

        # Auto‑Scaling Engine
        self.platform_scaler = PlatformAutoScaler(logger=logger)


    def think(self, context):
        reasoning_output = self.reasoning.think(context)

        if self.logger:
            self.logger.info("UnifiedBrain: reasoning completed.")

        return {
            "status": "thinking_complete",
            "reasoning": reasoning_output
        }


    def run_cycle(self, market):
        if self.logger:
            self.logger.info("UnifiedBrain: running full cycle.")

        # 1) Run orchestrator (designs, trends, collections…)
        cycle_output = self.orchestrator.run_cycle(market)

        # 2) Generate TikTok video
        video_output = self.video_engine.generate(
            design_path="assets/sample_design.png",
            text_lines=[
                "🔥 New Trending Design",
                "Made by AI POD Empire",
                "Available Now!"
            ],
            output_path="output/tiktok_video.mp4"
        )

        # 3) REAL TikTok Publishing
        marketing_output = self.marketing.distribute(
            video_path="output/tiktok_video.mp4"
        )

        # 4) Analytics Engine
        analytics_output = self.analytics.full_report(
            cycle_output=cycle_output,
            marketing_output=marketing_output
        )

        # 5) Auto‑Scaling Engine
        scaling_output = self.platform_scaler.analyze(
            marketing_results=marketing_output.get("tiktok", {})
        )

        # 6) Save insights to memory
        self.memory.save({
            "insights": ["Cycle completed successfully"],
            "strategy": "Updated after full cycle"
        })

        return {
            "status": "cycle_complete",
            "output": cycle_output,
            "tiktok_video": video_output,
            "marketing": marketing_output,
            "analytics": analytics_output,
            "scaling": scaling_output
        }
