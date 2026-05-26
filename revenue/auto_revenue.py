class AutoRevenue:
    def __init__(self, logger=None):
        self.logger = logger

    def optimize(self, sales_data):
        """
        Analyzes sales data and returns revenue optimization suggestions.
        """

        best_sellers = sales_data.get("best_sellers", [])
        low_performers = sales_data.get("low_performers", [])
        ad_spend = sales_data.get("ad_spend", 0)
        revenue = sales_data.get("revenue", 0)

        suggestions = {
            "increase_budget_for": best_sellers[:3],
            "reduce_budget_for": low_performers[:3],
            "pricing_recommendation": "Increase price by 10% for top sellers",
            "ad_strategy": "Shift budget to high-performing niches",
            "expected_growth": f"{round(revenue * 0.15, 2)} USD"
        }

        if self.logger:
            self.logger.info("AutoRevenue: optimization completed.")

        return suggestions
