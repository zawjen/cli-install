import time

class Logger:
    """Logger class for logging important or long-running steps."""
    def log(self, message, start_time):
        try:
            # Calculate elapsed time in seconds
            time_spent = round(time.time() - start_time, 2)
            print(f"{message} - Time spent: {time_spent} seconds")
        except Exception as e:
            print(f"Logging failed: {e}")
