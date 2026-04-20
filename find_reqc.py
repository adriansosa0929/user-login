import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'children:"Request Consultation"', text)
for m in matches:
    print(text[max(0, m.start()-100):min(len(text), m.end()+10)])

