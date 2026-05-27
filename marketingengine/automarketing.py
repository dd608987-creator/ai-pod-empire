import random
from tiktokpublisher.tiktok_api import TikTokPublisher

class AutoMarketingEngine:
    def __init__(self, token_manager=None, logger=None):
        self.logger = logger
        self.publisher = TikTokPublisher(token_manager, logger=logger)

    def prepare_post(self, video_path, caption):
        return {
            "video": video_path,
            "caption": caption,
            "status": "ready_for_posting"
        }

    def publish_tiktok(self, post_package):
        upload = self.publisher.upload_video(post_package["video"])

        if upload["status"] != "uploaded":
            return upload

        publish = self.publisher.publish(upload["upload_id"], post_package["caption"])

        return publish

    def distribute(self, video_path):
        caption = random.choice([
            "🔥 New AI‑Generated Design!",
            "🚀 Trending Now!",
            "✨ Limited Edition Drop!",
            "💥 Viral POD Collection!"
        ])

        post_package = self.prepare_post(video_path, caption)

        tiktok_result = self.publish_tiktok(post_package)

        return {
            "status": "distribution_complete",
            "tiktok": tiktok_result
        }
