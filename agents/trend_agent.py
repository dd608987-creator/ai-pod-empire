from agents.ai_agent_base import AIAgentBase

class TrendAgent(AIAgentBase):
    def generate(self, market="US"):
        prompt = f"""
        Get top POD trends for market: {market}.
        Return:
        - trending niches
        - trending keywords
        - trending styles
        - trending products
        Return JSON only.
        """
        return self.ask(prompt)
