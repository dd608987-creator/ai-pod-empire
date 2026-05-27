import requests
import json


class TikTokPublisher:
    def __init__(self, token_manager, logger=None):
        self.token_manager = token_manager
        self.logger = logger

        self.upload_url = "https://open.tiktokapis.com/v2/video/upload/"
        self.publish_url = "https://open.tiktokapis.com/v2/video/publish/"

    def upload_video(self, video_path):
        """
        Uploads a video file to TikTok servers.
        """

        headers = {
            "Authorization": f"Bearer {self.token_manager.get_token()}"
        }

        files = {
            "video": open(video_path, "rb")
        }

        response = requests.post(self.upload_url, headers=headers, files=files)

        if response.status_code != 200:
            if self.logger:
                self.logger.error(f"TikTok upload error: {response.text}")
            return {
                "status": "error",
                "details": response.text
            }

        data = response.json().get("data", {})
        upload_id = data.get("upload_id")

        if self.logger:
            self.logger.info(f"TikTok upload success. upload_id={upload_id}")

        return {
            "status": "uploaded",
            "upload_id": upload_id
        }

    def publish(self, upload_id, caption):
        """
        Publishes an uploaded video to TikTok.
        """

        headers = {
            "Authorization": f"Bearer {self.token_manager.get_token()}",
            "Content-Type": "application/json"
        }

        payload = {
            "upload_id": upload_id,
            "text": caption
        }

        response = requests.post(self.publish_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            if self.logger:
                self.logger.error(f"TikTok publish error: {response.text}")
            return {
                "status": "error",
                "details": response.text
            }

        data = response.json().get("data", {})
        video_id = data.get("video_id")

        if self.logger:
            self.logger.info(f"TikTok publish success. video_id={video_id}")

        return {
            "status": "published",
            "video_id": video_id
        }
