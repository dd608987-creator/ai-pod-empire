import requests
import json

class TikTokPublisher:
    def __init__(self, access_token, advertiser_id=None, logger=None):
        self.access_token = access_token
        self.advertiser_id = advertiser_id
        self.logger = logger

        self.upload_url = "https://open.tiktokapis.com/v2/video/upload/"
        self.publish_url = "https://open.tiktokapis.com/v2/video/publish/"

    def upload_video(self, video_path):
        """
        Uploads a video to TikTok servers.
        """

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        files = {
            "video": open(video_path, "rb")
        }

        response = requests.post(self.upload_url, headers=headers, files=files)

        if response.status_code != 200:
            return {"status": "error", "details": response.text}

        upload_id = response.json().get("data", {}).get("upload_id")

        return {
            "status": "uploaded",
            "upload_id": upload_id
        }

    def publish(self, upload_id, caption):
        """
        Publishes the uploaded video to TikTok.
        """

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "upload_id": upload_id,
            "text": caption
        }

        response = requests.post(self.publish_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            return {"status": "error", "details": response.text}

        return {
            "status": "published",
            "video_id": response.json().get("data", {}).get("video_id")
        }
