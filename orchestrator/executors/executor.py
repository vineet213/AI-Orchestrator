from orchestrator.connectors.opencode.adapter import OpenCodeAdapter


class Executor:
    def __init__(self):
        self.adapter = OpenCodeAdapter()

    def execute(self, task):
        return self.adapter.run(task.description)