import re
import io
import subprocess

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'rb') as f:
    data = f.read()

# Let's extract all the `import` statements at the top
m = re.search(b'export\{', data)
print("File length:", len(data))

# Let's see if we can find any syntax errors using the python jsmin/esprima package?
# Probably not installed.
