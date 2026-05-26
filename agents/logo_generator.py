from agents.ai_agent_base import AIAgentBase

class LogoGenerator(AIAgentBase):
    def generate(self, brand_name):
        prompt = f"""
        Create logo concepts for brand: {brand_name}.
        Return JSON only.
        """
        return self.ask(prompt)
