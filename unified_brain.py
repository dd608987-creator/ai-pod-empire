from orchestrator.orchestrator import Orchestrator
from reasoning.reasoning_core import ReasoningCore

class UnifiedBrain:
    def __init__(self, agents, memory, autoscaler, autolearn, autorevenue, autodesevo, logger=None):
        self.agents = agents
        self.memory = memory
        self.autoscaler = autoscaler
        self.autolearn = autolearn
        self.autorevenue = autorevenue
        self.autodesevo = autodesevo
        self.logger = logger

        self.reasoning = ReasoningCore(logger=logger)

        self.orchestrator = Orchestrator(
            agents=agents,
            memory=memory,
            autoscaler=autoscaler,
            autolearn=autolearn,
            autorevenue=autorevenue,
            autodesevo=autodesevo,
            logger=logger
        )

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

        cycle_output = self.orchestrator.run_cycle(market)

        # Save insights to memory
        self.memory.save({
            "insights": ["Cycle completed successfully"],
            "strategy": "Updated after full cycle"
        })

        return {
            "status": "cycle_complete",
            "output": cycle_output
        }
