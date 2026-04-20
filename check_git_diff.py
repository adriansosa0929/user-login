import subprocess
import os
os.chdir('..')
print(subprocess.run(['git', 'diff', 'index-uhv_Skau.js'], capture_output=True, text=True, encoding='utf-8').stdout)
