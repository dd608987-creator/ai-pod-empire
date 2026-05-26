from agents.ai_agent_base import AIAgentBase

class NicheAgent(AIAgentBase):
    def analyze(self, trends):
        prompt = f"""
        Analyze these trends:
        {trends}

        Return:
        - best niches
        - competition level
        - demand level
        - POD fit
        Return JSON only.
        """
        return self.ask(prompt)
