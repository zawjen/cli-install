import os
import subprocess
import time
from sdk.logger import Logger

class Task:
    """Base Task class. Derived tasks should implement the execute method."""
    def __init__(self):
        self.logger = Logger()
        
    def execute(self, task):
        raise NotImplementedError("Subclasses must implement this method.")
