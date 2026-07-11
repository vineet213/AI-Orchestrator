from rich.console import Console

from orchestrator.core.config import Config
from orchestrator.models.task import Task
from orchestrator.providers.ollama import OllamaProvider
from orchestrator.workflows.workflow import Workflow


class Engine:
    def __init__(self):
        self.console = Console()
        self.config = Config()

        self.provider = OllamaProvider()
        self.workflow = Workflow(self.provider)

    def start(self):
        project_name = self.config.get("project", {}).get("name", "Unknown")

        self.console.print(f"[cyan]Loading {project_name}...[/cyan]")

        self.provider.connect()

        self.console.print("[green]✓ Ollama Connected[/green]")
        self.console.print("[green]✓ Workflow Initialized[/green]")

        task = Task(
            title="Introduction",
            description="Introduce yourself in one sentence."
        )

        response = self.workflow.execute(task)

        self.console.print("\n[bold green]Response:[/bold green]")
        self.console.print(response)

        self.console.print(f"\nTask Status: {task.status}")

        self.console.print(
            f"\n[bold cyan]{project_name} Ready[/bold cyan]"
        )