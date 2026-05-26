from agents.ai_agent_base import AIAgentBase

class CollectionAgent(AIAgentBase):
    def generate(self, niche):
        prompt = f"""
        Create a POD collection for niche: {niche}.
        Include:
        - collection name
        - 10 products
        - design style
        - color palette
        Return JSON only.
        """
        return self.ask(prompt)
