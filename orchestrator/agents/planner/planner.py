from orchestrator.models.task import Task


class Planner:
    def __init__(self, provider):
        self.provider = provider

    def plan(self, task: Task) -> Task:
        prompt = f"""
You are a senior software architect.

Break the following software development task into a concise numbered implementation plan.

Rules:
- Output only the numbered steps.
- Keep each step short.
- Do not explain your reasoning.

Task:
{task.description}
"""

        plan = self.provider.chat(prompt)

        task.steps = [
            line.strip()
            for line in plan.splitlines()
            if line.strip()
        ]

        return task