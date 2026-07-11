import ollama

from orchestrator.providers.base import Provider


class OllamaProvider(Provider):
    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model

    def connect(self):
        try:
            models = ollama.list()

            if not models.models:
                raise RuntimeError("No Ollama models found.")

            return True

        except Exception as e:
            raise RuntimeError(
                "Failed to connect to Ollama. "
                "Ensure the Ollama server is running and at least one model is installed."
            ) from e

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