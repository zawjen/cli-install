import os
from sdk.task import Task
import time


class TaskInstall(Task):
    """TaskInstall downloads the specified exe, msi, etc. and runs it to install."""
    def execute(self, task):
        start_time = time.time()
        try:
            url = task.get('url')
            if not url:
                raise ValueError("No URL provided for install task")
            # Download the file using curl (or another downloader in a real implementation)
            download_cmd = f"curl -O {url}"
            os.system(download_cmd)
            # Extract the filename and execute it to perform installation
            filename = url.split('/')[-1]
            os.system(filename)
        except Exception as e:
            self.logger.log(f"TaskInstall error: {e}", start_time)