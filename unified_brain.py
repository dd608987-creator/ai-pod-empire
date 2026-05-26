from orchestrator.orchestrator import Orchestrator
from reasoning.reasoning_core import ReasoningCore
from video_engine.tiktok_video_generator import TikTokVideoGenerator

class UnifiedBrain:
    def __init__(self, agents, memory, autoscaler, autolearn, autorevenue, autodesevo, logger=None):
        self.agents = agents
        self.memory = memory
        self.autoscaler = autoscaler
        self.autolearn = autolearn
        self.autorevenue = autorevenue
        self.autodesevo = autodesevo
        self.logger = logger

        # Reasoning engine
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

    def think(self, context):
        """
        Unified reasoning layer.
        """
        reasoning_output = self.reasoning.think(context)

        if self.logger:
            self.logger.info("UnifiedBrain: reasoning completed.")

        return {
            "status": "thinking_complete",
            "reasoning": reasoning_output
        }

    def run_cycle(self, market):
        """
        Runs the full empire cycle through the orchestrator.
        """
        if self.logger:
            self.logger.info("UnifiedBrain: running full cycle.")

        # Run orchestrator
        cycle_output = self.orchestrator.run_cycle(market)

        # Generate TikTok video
        video_output = self.video_engine.generate(
            design_path="assets/sample_design.png",
            text_lines=[
                "🔥 New Trending Design",
                "Made by AI POD Empire",
                "Available Now!"
            ],
            output_path="output/tiktok_video.mp4"
        )

        # Save insights to memory
        self.memory.save({
            "insights": ["Cycle completed successfully"],
            "strategy": "Updated after full cycle"
        })

        return {
            "status": "cycle_complete",
            "output": cycle_output,
            "tiktok_video": video_output
        }
