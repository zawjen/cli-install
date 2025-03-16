# cli-install
Installs zawjen web, mobile and desktop development environment

## Tech Stack
- **Programming Language:** Python

## Project Structure
- All classes must be under the `sdk` folder.
- The program starts from **main.py**.

## Command Line Arguments

| Argument         | Description                                                        | Type                | Default       |
| ---------------- | ------------------------------------------------------------------ | ------------------- | ------------- |
| `--folders`      | Optional comma-separated list of JSON Task folder paths to install | String (comma list) | None          |
| `--files`        | Optional comma-separated list of JSON Task file paths to install   | String (comma list) | None          |
| `--thread-count` | Optional number of threads to execute tasks                        | Integer             | 1             |
| `--git-root`     | Optional path of git root folder                                   | String              | C:\zawjen\git |

## Class Design and Feature Details 

- **CliArgs**  
  A command line argument parser that uses the above arguments.

- **TaskManager**  
  Iterates over the list of folders and files. It creates `--thread-count` number of threads for the **TaskRunner** by passing it each task file name. If not specified, one thread is used by default.

- **Logger**  
  Provides a method `log(self, message, start_time)` that logs important or long-running steps by calculating time spent.

- **TaskRunner**  
  Reads a JSON file containing an array of tasks and executes each one by invoking the proper Task class.

- **Task (Base Class)** and **Task Types**  
  Each task is defined by a `type` attribute which could be:  
  - **install**: Download and run an installer (exe, msi, etc.).  
  - **git**: Execute a git pull (or clone if missing) for the repo specified in the `url` attribute to the location defined by `--git-root`.  
  - **command**: Run a specified PowerShell, batch, or bash command using the attribute `command`.  
  - **script**: Execute a file (absolute or relative) provided in the `path` attribute.

## Sample Task Json

```json
[
    {
        "type": "install",
        "url": [
            "http://example1.com/installer.exe",
            "http://example2.com/installer.exe",
            "http://example3.com/installer.exe",
        ]
    },
    {
        "type": "git",
        "url": [
            "https://github.com/zawjen/dataset-service",
            "https://github.com/zawjen/ds-lisan-ul-arab",
            "https://github.com/zawjen/cli-dataset-tagger"
        ]
    },
    {
        "type": "command",
        "command": [
            "echo Hello, World!",
            "dir",
            "ping 127.0.0.1 -n 1"
        ]
    },
    {
        "type": "script",
        "path": [
            "./run_script1.sh",
            "./run_script2.sh",
            "./run_script3.sh"
        ]
    },
    {
        "type": "browser",
        "url": [
            "http://example1.com",
            "http://example2.com",
            "http://example3.com"
        ]
    },
    {
        "type": "explorer",
        "path": [
            "C:\\",
            "D:\\"
        ]
    }
]
  ```