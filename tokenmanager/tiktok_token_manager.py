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
        """
        Checks if the current access token is expired.
        """
        return time.time() >= self.expires_at

    def refresh(self):
        """
        Refreshes TikTok access token using the refresh_token.
        """

        payload = {
            "client_key": self.client_key,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self.refresh_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            if self.logger:
                self.logger.error(f"Token refresh error: {response.text}")
            return {
                "status": "error",
                "details": response.text
            }

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
        """
        Returns a valid access token.
        Refreshes automatically if expired.
        """

        if self.access_token is None or self.is_expired():
            self.refresh()

        return self.access_token
