import shutil
import subprocess


class OpenCodeAdapter:
    def __init__(self):
        self.executable = shutil.which("opencode")

        if self.executable is None:
            raise RuntimeError("OpenCode executable not found.")

    def run(self, prompt: str):
        result = subprocess.run(
            [self.executable, "run", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }