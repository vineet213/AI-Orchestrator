import uuid
import requests


class OpenCodeSession:
    def __init__(
        self,
        session_id=None,
        host="http://127.0.0.1:4096",
        agent="build",
        provider="opencode",
        model="big-pickle",
    ):
        self.host = host.rstrip("/")
        self.session_id = session_id or str(uuid.uuid4())
        self.agent = agent
        self.provider = provider
        self.model = model

    def send_prompt(self, prompt: str):
        url = f"{self.host}/session/{self.session_id}/prompt_async"

        payload = {
            "agent": self.agent,
            "messageID": str(uuid.uuid4()),
            "model": {
                "providerID": self.provider,
                "modelID": self.model,
            },
            "parts": [
                {
                    "type": "text",
                    "text": prompt,
                }
            ],
        }

        response = requests.post(url, json=payload)

        response.raise_for_status()

        return response.status_code