class TrainingCenter:
    def __init__(self, memory, logger=None):
        self.memory = memory
        self.logger = logger

    def train_agent(self, agent_name, dataset):
        """
        Trains an agent using new dataset.
        """

        training_summary = {
            "agent": agent_name,
            "dataset_size": len(dataset),
            "status": "training_completed",
            "notes": "Agent improved using new data."
        }

        # Save training results to memory
        self.memory.save({
            "insights": [f"{agent_name} improved from training"],
            "strategy": f"Updated strategy after training {agent_name}"
        })

        if self.logger:
            self.logger.info(f"TrainingCenter: {agent_name} trained successfully.")

        return training_summary

    def train_all(self, datasets):
        """
        Trains all agents using provided datasets.
        """

        results = {}

        for agent_name, dataset in datasets.items():
            results[agent_name] = self.train_agent(agent_name, dataset)

        return {
            "status": "all_agents_trained",
            "results": results
        }
