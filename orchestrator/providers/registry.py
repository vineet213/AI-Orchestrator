from orchestrator.providers.ollama import OllamaProvider


class ProviderRegistry:
    _providers = {
        "ollama": OllamaProvider,
    }

    @classmethod
    def create(cls, name: str):
        if name not in cls._providers:
            available = ", ".join(cls._providers.keys())
            raise ValueError(
                f"Unknown provider '{name}'. Available providers: {available}"
            )

        return cls._providers[name]()