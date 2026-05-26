from agents.ai_agent_base import AIAgentBase

class BrandBuilder(AIAgentBase):
    def build(self, niche):
        prompt = f"""
        Build a POD brand for niche: {niche}.
        Include:
        - brand name
        - brand story
        - color palette
        - typography
        Return JSON only.
        """
        return self.ask(prompt)
