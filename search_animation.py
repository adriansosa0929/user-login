import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.finditer(r'animate:\{.*?\}', text)
for i, match in enumerate(m):
    s = match.group(0)
    if 'y:[' in s:
        print("Float animation context:", text[max(0, match.start()-100):min(len(text), match.end()+100)])
        if i > 10: break
