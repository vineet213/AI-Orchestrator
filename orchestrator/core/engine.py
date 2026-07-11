from rich.console import Console

from orchestrator.core.config import Config
from orchestrator.memory.memory import Memory
from orchestrator.models.task import Task
from orchestrator.providers.registry import ProviderRegistry
from orchestrator.workflows.workflow import Workflow


class Engine:
    def __init__(self):
        self.console = Console()
        self.config = Config()

        self.memory = Memory()

        self.provider_name = self.config.get(
            "provider", {}
        ).get("active", "ollama")

        self.provider = ProviderRegistry.create(self.provider_name)
        self.workflow = Workflow(self.provider)

    def start(self):
        project_name = self.config.get(
            "project", {}
        ).get("name", "Unknown")

        self.console.print(f"[cyan]Loading {project_name}...[/cyan]")

        self.provider.connect()

        self.console.print(f"[green]✓ Provider: {self.provider_name}[/green]")
        self.console.print("[green]✓ Workflow Initialized[/green]")
        self.console.print("[green]✓ Memory Initialized[/green]")

        task = Task(
            title="Introduction",
            description="Introduce yourself in one sentence."
        )

        response = self.workflow.execute(task)

        self.memory.save(task)

        self.console.print("\n[bold blue]Execution Plan:[/bold blue]")

        if task.steps:
            for i, step in enumerate(task.steps, start=1):
                self.console.print(f"{i}. {step}")
        else:
            self.console.print("No execution plan generated.")

        self.console.print("\n[bold green]Response:[/bold green]")
        self.console.print(response)

        self.console.print(f"\nTask Status: {task.status}")

        self.console.print(
            f"\n[bold cyan]{project_name} Ready[/bold cyan]"
        )