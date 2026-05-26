import requests

class GoogleAIAgent:
    def __init__(self, api_key, model="gemini-2.0-pro-exp"):
        self.api_key = api_key
        self.model = model

    def ask(self, prompt):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload)
        return response.json()
