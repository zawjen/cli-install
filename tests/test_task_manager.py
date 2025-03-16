import os
import json
from sdk.task_manager import TaskManager
from sdk.logger import Logger

class DummyTaskRunner:
    def run_task(self, file_path):
        print(f'Running task file: {file_path}')

def test_task_manager(tmp_path, monkeypatch):
    # Create temporary folder with one JSON file containing a dummy task.
    task_folder = tmp_path / 'tasks'
    task_folder.mkdir()
    task_file = task_folder / 'task1.json'
    task_file.write_text(json.dumps([{""type"": ""command", ""command"": ""echo test""}]))

    folders = [str(task_folder)]
    files = []
    logger = Logger()
    task_runner = DummyTaskRunner()

    outputs = []
    monkeypatch.setattr('builtins.print', lambda s: outputs.append(s))
    tm = TaskManager(folders, files, 2, task_runner, logger)
    tm.run()

    assert any('Running task file:' in out for out in outputs)
