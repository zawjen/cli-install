import subprocess
import time

from sdk.task import Task


class TaskScript(Task):
    """
    TaskScript executes script files provided in the 'path' attribute.
    """
    def execute(self, task):
        start_time = time.time()
        try:
            paths = task.get('path', [])
            if not paths:
                raise ValueError("No paths provided for script task")
            if isinstance(paths, str):
                paths = [paths]
                
            for path in paths:
                subprocess.run(path, shell=True, check=True)
        except subprocess.CalledProcessError as cpe:
            self.logger.log(f"TaskScript subprocess error: {cpe}", start_time)
        except Exception as e:
            self.logger.log(f"TaskScript error: {e}", start_time)