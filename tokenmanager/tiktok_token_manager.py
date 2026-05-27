import time
import requests
import json

class TikTokTokenManager:
    def __init__(self, client_key, client_secret, refresh_token, logger=None):
        self.client_key = client_key
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = None
        self.expires_at = 0
        self.logger = logger

        self.refresh_url = "https://open.tiktokapis.com/v2/oauth/token/"

    def is_expired(self):
        return time.time() >= self.expires_at

    def refresh(self):
        payload = {
            "client_key": self.client_key,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(self.refresh_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            return {"status": "error", "details": response.text}

        data = response.json().get("data", {})

        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")
        self.expires_at = time.time() + data.get("expires_in", 3600)

        if self.logger:
            self.logger.info("TokenManager: token refreshed successfully.")

        return {
            "status": "refreshed",
            "access_token": self.access_token,
            "expires_in": data.get("expires_in")
        }

    def get_token(self):
        if self.access_token is None or self.is_expired():
            self.refresh()

        return self.access_token
