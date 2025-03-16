#!/usr/bin/env python
import sys
from sdk.cli_args import CliArgs
from sdk.logger import Logger
from sdk.task_manager import TaskManager
from sdk.task_runner import TaskRunner

def main():
    # Parse CLI arguments
    cli_args = CliArgs()
    args = cli_args.parse_args()

    # Initialize Logger
    logger = Logger()

    # Create TaskRunner instance; pass git_root from args
    task_runner = TaskRunner(logger, args.git_root)

    # Get list of folders and files from CLI arguments
    folders = CliArgs.get_folders(args)
    files = CliArgs.get_files(args)

    # Create and run TaskManager
    task_manager = TaskManager(folders, files, args.thread_count, task_runner, logger)
    task_manager.run()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Fatal error: {e}', file=sys.stderr)
