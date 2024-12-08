import time
import subprocess

timestamp = time.time()
subprocess.check_call(f'echo TIMESTAMP={timestamp} >> "$GITHUB_ENV"', shell=True)
print(timestamp)
