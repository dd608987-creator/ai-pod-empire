from agents.ai_agent_base import AIAgentBase

class GlobalExpansionAgent(AIAgentBase):
    def expand(self, country):
        prompt = f"""
        Analyze POD market in {country}.
        Return:
        - niches
        - pricing
        - culture notes
        - design styles
        Return JSON only.
        """
        return self.ask(prompt)
