import subprocess
import os
os.chdir('..')
with open('user-login/diff.txt', 'wb') as f:
    f.write(subprocess.run(['git', 'diff', 'index-uhv_Skau.js'], capture_output=True).stdout)
