class AutoLearning:
    def __init__(self, memory, logger=None):
        self.memory = memory
        self.logger = logger

    def learn(self, brain_output):
        """
        Learns from Unified Brain output and stores insights.
        """
        insights = brain_output.get("insights", [])
        strategy = brain_output.get("updated_strategy", "")

        self.memory.save({
            "insights": insights,
            "strategy": strategy
        })

        if self.logger:
            self.logger.info("AutoLearning: insights saved.")

        return {
            "status": "learned",
            "saved": True,
            "insights_count": len(insights)
        }
