import os
from sdk.task import Task
import time

class TaskInstall(Task):
    """TaskInstall downloads the specified exe, msi, etc. and runs it to install."""
    def execute(self, task):
        start_time = time.time()
        try:
            urls = task.get('url', [])
            if not urls:
                raise ValueError("No URLs provided for install task")
            if isinstance(urls, str):
                urls = [urls]

            # Check if curl is installed by trying to run curl --version
            curl_check = os.system("curl --version > nul 2>&1")
            if curl_check != 0:
                # Curl not found, attempt to install it silently
                if os.name == 'nt':  # Windows
                    os.system("winget install -e --id cURL.cURL --silent")
                else:  # Linux/Mac
                    os.system("apt-get install -y curl > /dev/null 2>&1 || yum install -y curl > /dev/null 2>&1")

            for url in urls:
                # Download the file using curl
                download_cmd = f"curl -O {url}"
                os.system(download_cmd)
                
                # Extract the filename and execute it to perform installation
                filename = url.split('/')[-1]
                os.system(filename)
        except Exception as e:
            self.logger.log(f"TaskInstall error: {e}", start_time)