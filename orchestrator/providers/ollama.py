import ollama

from orchestrator.providers.base import Provider


class OllamaProvider(Provider):
    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model

    def connect(self):
        ollama.list()
        return True

    def chat(self, prompt: str):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]