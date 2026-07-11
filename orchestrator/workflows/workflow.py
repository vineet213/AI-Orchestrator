from orchestrator.agents.planner.planner import Planner
from orchestrator.executors.executor import Executor
from orchestrator.models.task import Task


class Workflow:
    def __init__(self, provider):
        self.provider = provider
        self.planner = Planner(provider)
        self.executor = Executor()

    def execute(self, task: Task):
        task.status = "planning"

        task = self.planner.plan(task)

        task.status = "executing"

        result = self.executor.execute(task)

        task.status = "completed"

        return result