class AdsAutoScaler:
    def optimize(self, ads_data):
        return {
            "scale_up": ["ad_01"],
            "scale_down": ["ad_03"],
            "stop": ["ad_05"]
        }
