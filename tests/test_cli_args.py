import sys
from sdk.cli_args import CliArgs

def test_cli_args_parsing(monkeypatch):
    test_args = ['prog', '--folders', 'folder1,folder2', '--files', 'file1.json,file2.json', '--thread-count', '4', '--git-root', 'C:\test\git']
    monkeypatch.setattr(sys, 'argv', test_args)
    cli = CliArgs()
    args = cli.parse_args()
    assert args.folders == 'folder1,folder2'
    assert args.files == 'file1.json,file2.json'
    assert args.thread_count == 4
    assert args.git_root == r'C:\test\git'
    
def test_get_folders_and_files():
    class Args:
        folders = 'folder1,folder2'
        files = 'file1.json,file2.json'
    args = Args()
    folders = CliArgs.get_folders(args)
    files = CliArgs.get_files(args)
    assert folders == ['folder1', 'folder2']
    assert files == ['file1.json', 'file2.json']
