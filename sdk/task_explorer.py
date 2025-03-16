import os
import platform
from sdk.task import Task
import time


class TaskExplorer(Task):
    """TaskExplorer opens up the file explorer on Windows, Mac, and Linux for the given paths."""
    def execute(self, task):
        start_time = time.time()
        try:
            paths = task.get('path', [])
            if not paths:
                raise ValueError("No paths provided for explore task")
            if isinstance(paths, str):
                paths = [paths]

            system_platform = platform.system()
            for path in paths:
                if system_platform == "Windows":
                    # Windows: use explorer.exe
                    os.system(f'explorer "{path}"')
                elif system_platform == "Darwin":
                    # macOS: use open command
                    os.system(f'open "{path}"')
                elif system_platform == "Linux":
                    # Linux: use xdg-open command
                    os.system(f'xdg-open "{path}"')
                else:
                    raise OSError("Unsupported platform")
        except Exception as e:
            self.logger.log(f"TaskExplore error: {e}", start_time)
