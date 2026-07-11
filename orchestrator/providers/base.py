from abc import ABC, abstractmethod


class Provider(ABC):
    @abstractmethod
    def connect(self):
        """Connect to the provider."""

    @abstractmethod
    def chat(self, prompt: str):
        """Send a prompt and return the response."""