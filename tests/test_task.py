import os
import subprocess
from sdk.task import TaskInstall, TaskGit, TaskCommand, TaskScript

def test_task_install(monkeypatch):
    executed = []
    def fake_system(cmd):
        executed.append(cmd)
        return 0
    monkeypatch.setattr(os, 'system', fake_system)
    task = {""url"": ""http://example.com/installer.exe""}
    TaskInstall().execute(task)
    # Check that both the download and execution commands were issued
    assert any('curl -O' in cmd for cmd in executed)
    assert any('installer.exe' in cmd for cmd in executed)

def test_task_git(monkeypatch, tmp_path):
    executed = []
    def fake_system(cmd):
        executed.append(cmd)
        return 0
    monkeypatch.setattr(os, 'system', fake_system)
    monkeypatch.setattr(os.path, 'exists', lambda p: False)
    task = {""url"": ""http://example.com/repo.git""}
    git_root = str(tmp_path / 'git')
    TaskGit(git_root).execute(task)
    assert any('git clone' in cmd for cmd in executed)

def test_task_command(monkeypatch):
    executed = []
    def fake_run(cmd, shell, check):
        executed.append(cmd)
        return 0
    monkeypatch.setattr(subprocess, 'run', fake_run)
    task = {""command"": ""echo test""}
    TaskCommand().execute(task)
    assert "echo test" in executed

def test_task_script(monkeypatch):
    executed = []
    def fake_run(cmd, shell, check):
        executed.append(cmd)
        return 0
    monkeypatch.setattr(subprocess, 'run', fake_run)
    task = {""path"": ""echo script""}
    TaskScript().execute(task)
    assert "echo script" in executed
