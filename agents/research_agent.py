from agents.ai_agent_base import AIAgentBase

class ResearchAgent(AIAgentBase):
    def research(self, niche):
        prompt = f"""
        Research POD products for niche: {niche}.
        Return:
        - best products
        - pricing
        - competition
        - demand
        Return JSON only.
        """
        return self.ask(prompt)
