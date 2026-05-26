from agents.ai_agent_base import AIAgentBase

class MarketingAgent(AIAgentBase):
    def generate(self, product):
        prompt = f"""
        Create a marketing pack for product: {product}.
        Include:
        - SEO title
        - SEO description
        - 13 Etsy tags
        - social media captions
        Return JSON only.
        """
        return self.ask(prompt)
