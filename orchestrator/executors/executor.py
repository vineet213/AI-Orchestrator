from orchestrator.connectors.opencode.adapter import OpenCodeAdapter


class Executor:
    def __init__(self):
        self.adapter = OpenCodeAdapter()

    def execute(self, task):
        prompt = task.description

        if task.steps:
            prompt += "\n\nImplementation Plan:\n"

            for step in task.steps:
                prompt += f"{step}\n"

        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n============================\n")

        return self.adapter.run(prompt)