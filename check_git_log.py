import subprocess
import os
os.chdir('..')
print(subprocess.run(['git', 'log', '-n', '5', '--oneline'], capture_output=True, text=True).stdout)
