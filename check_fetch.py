import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('fetch(')
if idx != -1:
    print(text[idx-200:idx+300])

m = re.finditer(r'fetch\(', text)
for match in m:
    print("Found fetch at", match.start())
    print(text[match.start():match.start()+100])
