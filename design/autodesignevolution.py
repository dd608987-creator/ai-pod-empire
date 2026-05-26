class AutoDesignEvolution:
    def __init__(self, logger=None):
        self.logger = logger

    def evolve(self, design_data):
        """
        Evolves design style based on performance.
        """
        best_colors = design_data.get("best_colors", ["black", "white"])
        best_fonts = design_data.get("best_fonts", ["sans-serif"])
        best_styles = design_data.get("best_styles", ["minimal"])

        evolved_style = {
            "color_palette": best_colors[:3],
            "typography": best_fonts[:2],
            "style": best_styles[0],
            "notes": "Design evolved based on top-performing products."
        }

        if self.logger:
            self.logger.info("AutoDesignEvolution: style updated.")

        return evolved_style
