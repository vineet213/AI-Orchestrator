from orchestrator.models.task import Task


class Planner:
    def __init__(self, provider):
        self.provider = provider

    def plan(self, task: Task):
        prompt = f"""
You are an expert software architect.

Break the following task into a numbered implementation plan.

Task:
{task.description}
"""

        return self.provider.chat(prompt)