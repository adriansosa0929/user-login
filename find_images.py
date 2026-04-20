import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find where kam_ocular_implant.png is used
matches = re.finditer(r'kam_ocular_implant\.png', text)
for m in matches:
    print(text[max(0, m.start() - 200) : min(len(text), m.end() + 200)])
