from agents.ai_agent_base import AIAgentBase

class MockupAgent(AIAgentBase):
    def generate(self, design_url):
        prompt = f"""
        Create mockup ideas for design: {design_url}.
        Include:
        - lifestyle mockups
        - studio mockups
        - product mockups
        Return JSON only.
        """
        return self.ask(prompt)
