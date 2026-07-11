from orchestrator.agents.planner.planner import Planner
from orchestrator.models.task import Task


class Workflow:
    def __init__(self, provider):
        self.provider = provider
        self.planner = Planner(provider)

    def execute(self, task: Task):
        task.status = "planning"

        task = self.planner.plan(task)

        task.status = "running"

        response = self.provider.chat(task.description)

        task.status = "completed"

        return response