import json
from sdk.task_runner import TaskRunner
from sdk.logger import Logger

def dummy_execute(self, task):
    print(f'Executing {task.get("type")}')

def test_run_task(tmp_path, monkeypatch):
    # Create a temporary JSON file with a list of tasks
    tasks = [
        {""type"": ""install", ""url"": ""http://example.com/file.exe""},
        {""type"": ""git", ""url"": ""http://example.com/repo.git""},
        {""type"": ""command", ""command"": ""echo test""},
        {""type"": ""script", ""path"": ""echo script""}
    ]
    task_file = tmp_path / "test_tasks.json"
    task_file.write_text(json.dumps(tasks))

    # Monkey-patch the execution methods of each Task type so no real command is run.
    monkeypatch.setattr('sdk.task.TaskInstall.execute', dummy_execute)
    monkeypatch.setattr('sdk.task.TaskGit.execute', dummy_execute)
    monkeypatch.setattr('sdk.task.TaskCommand.execute', dummy_execute)
    monkeypatch.setattr('sdk.task.TaskScript.execute', dummy_execute)

    logger = Logger()
    task_runner = TaskRunner(logger, "dummy_git_root")
    outputs = []
    monkeypatch.setattr('builtins.print', lambda s: outputs.append(s))
    task_runner.run_task(str(task_file))

    # Verify that each task type was "executed" (printed) at least once.
    assert any('Executing install' in out for out in outputs)
    assert any('Executing git' in out for out in outputs)
    assert any('Executing command' in out for out in outputs)
    assert any('Executing script' in out for out in outputs)
