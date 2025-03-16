import subprocess
import time

from sdk.task import Task


class TaskCommand(Task):
    """TaskCommand runs a specified command (PowerShell, batch, or bash) as provided in the 'command' attribute."""
    def execute(self, task):
        start_time = time.time()
        try:
            command = task.get('command')
            if not command:
                raise ValueError("No command provided for command task")
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as cpe:
            self.logger.log(f"TaskCommand subprocess error: {cpe}", start_time)
        except Exception as e:
            self.logger.log(f"TaskCommand error: {e}", start_time)
            

