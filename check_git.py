import subprocess
import os
os.chdir('..')
print(subprocess.run(['git', 'status'], capture_output=True, text=True).stdout)
