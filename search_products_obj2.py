import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'gi=\{extremities:\{', text)
if m:
    print(text[m.start()+2000:m.start()+4000])

