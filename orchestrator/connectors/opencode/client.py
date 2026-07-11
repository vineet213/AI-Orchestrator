import requests


class OpenCodeClient:
    def __init__(self, host="http://127.0.0.1:4096"):
        self.host = host.rstrip("/")

    def connect(self):
        response = requests.get(f"{self.host}/global/health")
        response.raise_for_status()

        health = response.json()

        print("✓ Connected to OpenCode")
        print(f"Version: {health['version']}")

        return True

    def health(self):
        response = requests.get(f"{self.host}/global/health")
        response.raise_for_status()

        return response.json()