import shutil
import subprocess


class OpenCodeAdapter:
    def __init__(self):
        self.executable = shutil.which("opencode")

        if self.executable is None:
            raise RuntimeError("OpenCode executable not found.")

    def run(self, prompt: str):
        command = f'"{self.executable}" run "{prompt}"'

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }