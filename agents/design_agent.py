from agents.ai_agent_base import AIAgentBase

class DesignAgent(AIAgentBase):
    def generate(self, niche):
        prompt = f"""
        Generate 20 POD designs for niche: {niche}.
        Include:
        - design titles
        - design descriptions
        - style
        - color palette
        Return JSON only.
        """
        return self.ask(prompt)
