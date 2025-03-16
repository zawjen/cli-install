import subprocess
import time

from sdk.task import Task


class TaskScript(Task):
    """
    TaskScript executes a script file provided in the 'path' attribute.
    """
    def execute(self, task):
        start_time = time.time()
        try:
            path = task.get('path')
            if not path:
                raise ValueError("No path provided for script task")
            subprocess.run(path, shell=True, check=True)
        except subprocess.CalledProcessError as cpe:
            self.logger.log(f"TaskScript subprocess error: {cpe}", start_time)
        except Exception as e:
            self.logger.log(f"TaskScript error: {e}", start_time)
            