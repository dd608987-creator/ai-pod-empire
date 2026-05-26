class StoreManager:
    def publish(self, product, platform):
        return {
            "status": "published",
            "platform": platform,
            "product": product
        }
