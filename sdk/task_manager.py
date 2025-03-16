import threading
import os
import time

class TaskManager:
    """TaskManager iterates over lists of folders and files and creates threads for TaskRunner."""
    def __init__(self, folders, files, thread_count, task_runner, logger):
        self.folders = folders
        self.files = files
        self.thread_count = thread_count if thread_count > 0 else 1
        self.task_runner = task_runner
        self.logger = logger

    def run(self):
        start_time = time.time()
        tasks = []
        # Add all JSON files from provided folders
        for folder in self.folders:
            try:
                for file in os.listdir(folder):
                    if file.endswith('.json'):
                        tasks.append(os.path.join(folder, file))
            except Exception as e:
                self.logger.log(f"Error reading folder {folder}: {e}", start_time)
        # Add files provided directly via CLI
        tasks.extend(self.files)
        
        if not tasks:
            self.logger.log("No tasks to run", start_time)
            return
        
        threads = []
        # Limit thread count to number of tasks if there are fewer tasks than requested threads
        num_threads = min(self.thread_count, len(tasks))
        # Distribute tasks round-robin among threads
        for i in range(num_threads):
            thread_tasks = tasks[i::num_threads]
            thread = threading.Thread(target=self._run_tasks, args=(thread_tasks,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()

    def _run_tasks(self, tasks):
        start_time = time.time()

        for task_file in tasks:
            try:
                self.task_runner.run_task(task_file)
            except Exception as e:
                self.logger.log(f"Error running task file {task_file}: {e}", start_time)
