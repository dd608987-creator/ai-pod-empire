from agents.ai_agent_base import AIAgentBase

class VideoAgent(AIAgentBase):
    def generate(self, niche):
        prompt = f"""
        Create 10 viral TikTok/Reels video ideas for niche: {niche}.
        Return JSON only.
        """
        return self.ask(prompt)
