from orchestrator.models.task import Task


class Workflow:
    def __init__(self, provider):
        self.provider = provider

    def execute(self, task: Task):
        task.status = "running"

        response = self.provider.chat(task.description)

        task.status = "completed"

        return response