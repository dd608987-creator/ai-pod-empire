from orchestrator.orchestrator import Orchestrator
from reasoning.reasoning_core import ReasoningCore
from video_engine.TikTokVideoGenerator import TikTokVideoGenerator

from marketingengine.automarketing import AutoMarketingEngine
from analyticsengine.autoanalytics import AutoAnalyticsEngine
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

        # Orchestrator (يحتوي Auto‑Trend Hunter + Design Agent)
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

        # 1) Orchestrator: ترندات + تصميمات من الترند
        cycle_output = self.orchestrator.run_cycle(market)

        designs = cycle_output.get("designs", [])
        trends_data = cycle_output.get("trends", {})
        pod_trends = trends_data.get("pod_trends", [])

        # اختيار التصميم والترند الأساسي
        if designs:
            main_design = designs[0]
            main_trend = main_design.get("trend", "AI POD Empire")
            design_id = main_design.get("design_id", "design_default")
        else:
            main_trend = "AI POD Empire"
            design_id = "design_default"

        # 2) توليد فيديو TikTok مبني على التصميم + الترند
        # مبدئياً نفترض أن ملف التصميم موجود كصورة بنفس الـ design_id
        design_path = f"assets/{design_id}.png"

        video_output = self.video_engine.generate(
            design_path=design_path,
            text_lines=[
                f"🔥 {main_trend}",
                "Made by AI POD Empire",
                "Available Now!"
            ],
            output_path="output/tiktok_video.mp4"
        )

        # 3) النشر الحقيقي على TikTok
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

        # 6) حفظ الـ insights في الذاكرة
        self.memory.save({
            "insights": ["Cycle completed successfully"],
            "trend_used": main_trend,
            "design_used": design_id,
            "strategy": "Updated after full cycle"
        })

        return {
            "status": "cycle_complete",
            "market": market,
            "trend_used": main_trend,
            "design_used": design_id,
            "output": cycle_output,
            "tiktok_video": video_output,
            "marketing": marketing_output,
            "analytics": analytics_output,
            "scaling": scaling_output
        }
