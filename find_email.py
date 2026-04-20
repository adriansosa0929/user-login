import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'kamindustries', text)]
for m in matches:
    print("Found around:", text[max(0, m-50):min(len(text), m+50)])
