from agents.ai_agent_base import AIAgentBase

class StoreReplicator(AIAgentBase):
    def analyze(self, store_url):
        prompt = f"""
        Analyze POD store: {store_url}.
        Return:
        - best products
        - pricing
        - SEO
        - design styles
        Return JSON only.
        """
        return self.ask(prompt)
