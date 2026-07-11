import json
from pathlib import Path

from orchestrator.models.task import Task


class Memory:
    def __init__(self):
        self.path = Path("project_state.json")

    def save(self, task: Task):
        data = {
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "steps": task.steps,
        }

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not self.path.exists():
            return None

        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)