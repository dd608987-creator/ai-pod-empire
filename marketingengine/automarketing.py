import random
from tiktokpublisher.tiktok_api import TikTokPublisher


class AutoMarketingEngine:
    def __init__(self, token_manager=None, logger=None):
        self.logger = logger
        self.publisher = TikTokPublisher(token_manager, logger=logger)

    def prepare_post(self, video_path, caption):
        """
        Creates a post package before publishing.
        """
        return {
            "video": video_path,
            "caption": caption,
            "status": "ready_for_posting"
        }

    def publish_tiktok(self, post_package):
        """
        Handles REAL TikTok publishing:
        1) Upload video
        2) Publish video
        """

        # Step 1 — Upload
        upload = self.publisher.upload_video(post_package["video"])

        if upload["status"] != "uploaded":
            return {
                "status": "error",
                "step": "upload",
                "details": upload
            }

        # Step 2 — Publish
        publish = self.publisher.publish(
            upload_id=upload["upload_id"],
            caption=post_package["caption"]
        )

        if publish["status"] != "published":
            return {
                "status": "error",
                "step": "publish",
                "details": publish
            }

        return {
            "status": "success",
            "video_id": publish["video_id"]
        }

    def distribute(self, video_path):
        """
        Full distribution pipeline:
        - Generate caption
        - Prepare post
        - Publish to TikTok (REAL)
        """

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
