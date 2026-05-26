from unified_brain import UnifiedBrain
from memory.memory import Memory
from autoscaling.auto_scaler import AutoScaler
from autolearning.auto_learning import AutoLearning
from design.auto_design_evolution import AutoDesignEvolution
from revenue.auto_revenue import AutoRevenue

class EmpireOS:
    def __init__(self, agents, logger=None):
        self.memory = Memory()
        self.autoscaler = AutoScaler(logger=logger)
        self.autolearn = AutoLearning(memory=self.memory, logger=logger)
        self.autodesign = AutoDesignEvolution(logger=logger)
        self.autorevenue = AutoRevenue(logger=logger)

        self.brain = UnifiedBrain(
            agents=agents,
            memory=self.memory,
            autoscaler=self.autoscaler,
            autolearn=self.autolearn,
            autorevenue=self.autorevenue,
            autodesevo=self.autodesign,
            logger=logger
        )

    def run(self, market="US"):
        """
        Runs a full empire cycle:
        - trend analysis
        - design generation
        - mockups
        - collections
        - marketing
        - learning
        - scaling
        - revenue optimization
        - design evolution
        """
        return self.brain.run_cycle(market)
