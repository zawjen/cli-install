import argparse

class CliArgs:
    """CLI Arguments parser for the CLI Install Tool."""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Zawjen CLI Install Tool")
        self.parser.add_argument('--folders', type=str, help='Comma-separated list of JSON Task folder paths to install')
        self.parser.add_argument('--files', type=str, help='Comma-separated list of JSON Task file paths to install')
        self.parser.add_argument('--thread-count', type=int, default=1, help='Number of threads to execute tasks')
        self.parser.add_argument('--git-root', type=str, default=r'C:\zawjen\git', help='Path of git root folder')

    def parse_args(self):
        return self.parser.parse_args()

    @staticmethod
    def get_folders(args):
        if args.folders:
            return [folder.strip() for folder in args.folders.split(',')]
        return []

    @staticmethod
    def get_files(args):
        if args.files:
            return [file.strip() for file in args.files.split(',')]
        return []
