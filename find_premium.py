import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'onClick:([^}]+children:"Premium Clearance"\}?)', text)
for m in matches:
    print(m.group(1))

