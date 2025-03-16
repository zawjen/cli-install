import os
import time

from sdk.task import Task


class TaskGit(Task):
    """TaskGit performs a git pull for the specified repository."""
    def __init__(self, git_root):
        self.git_root = git_root

    def execute(self, task):
        start_time = time.time()
        try:
            repo_url = task.get('url')
            if not repo_url:
                raise ValueError("No repository URL provided for git task")
            repo_name = repo_url.split('/')[-1].replace('.git', '')
            destination = os.path.join(self.git_root, repo_name)
            if not os.path.exists(destination):
                os.system(f"git clone {repo_url} {destination}")
            else:
                # Change directory and perform git pull
                os.chdir(destination)
                os.system("git pull")
        except Exception as e:
            self.logger.log(f"TaskGit error: {e}", start_time)