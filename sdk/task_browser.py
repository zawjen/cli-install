import time
import webbrowser
from sdk.task import Task

class TaskBrowser(Task):
    """TaskBrowser opens up web browsers with the given URLs."""
    def execute(self, task):
        start_time = time.time()
        try:
            urls = task.get('url', [])
            if not urls:
                raise ValueError("No URLs provided for browser task")
            if isinstance(urls, str):
                urls = [urls]
                
            # Open each URL using the default web browser
            for url in urls:
                webbrowser.open(url)
        except Exception as e:
            self.logger.log(f"TaskBrowser error: {e}", start_time)
