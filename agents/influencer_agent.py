from agents.ai_agent_base import AIAgentBase

class InfluencerAgent(AIAgentBase):
    def generate(self, niche):
        prompt = f"""
        Generate influencer-style content ideas for niche: {niche}.
        Return JSON only.
        """
        return self.ask(prompt)
