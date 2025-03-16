import json
import time
from sdk.task import Task 
from sdk.task_browser import TaskBrowser
from sdk.task_explorer import TaskExplorer
from sdk.task_install import TaskInstall 
from sdk.task_git import TaskGit 
from sdk.task_command import TaskCommand 
from sdk.task_script import TaskScript 

class TaskRunner:
    """TaskRunner reads a JSON task file and executes each task based on its type."""
    def __init__(self, logger, git_root):
        self.logger = logger
        self.git_root = git_root

    def run_task(self, file_path):
        start_time = time.time()

        try:
            with open(file_path, 'r') as f:
                tasks = json.load(f)
        except Exception as e:
            self.logger.log(f"Failed to read {file_path}: {e}", start_time)
            return
        
        for task in tasks:
            self.execute_task(task)

    def execute_task(self, task):
        start_time = time.time()

        task_type = task.get('type').lower()

        try:
            if task_type == 'install':
                TaskInstall().execute(task)
            elif task_type == 'git':
                TaskGit(self.git_root).execute(task)
            elif task_type == 'command':
                TaskCommand().execute(task)
            elif task_type == 'script':
                TaskScript().execute(task)
            elif task_type == 'browser':
                TaskBrowser().execute(task)
            elif task_type == 'explorer':
                TaskExplorer().execute(task)
            else:
                self.logger.log(f"Unknown task type: {task_type}", start_time)
        except Exception as e:
            self.logger.log(f"Error executing task {task}: {e}", start_time)
