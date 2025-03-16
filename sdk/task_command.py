import subprocess
import time

from sdk.task import Task


class TaskCommand(Task):
    """TaskCommand runs a specified command (PowerShell, batch, or bash) as provided in the 'command' attribute.
    The command can be a single string or an array of commands to be executed sequentially."""
    def execute(self, task):
        start_time = time.time()
        try:
            command = task.get('command')
            if not command:
                raise ValueError("No command provided for command task")
            
            # Handle both single command (string) and multiple commands (list)
            commands = command if isinstance(command, list) else [command]
            
            for cmd in commands:
                subprocess.run(cmd, shell=True, check=True)
                
        except subprocess.CalledProcessError as cpe:
            self.logger.log(f"TaskCommand subprocess error: {cpe}", start_time)
        except Exception as e:
            self.logger.log(f"TaskCommand error: {e}", start_time)
            

