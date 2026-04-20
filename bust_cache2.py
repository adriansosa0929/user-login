import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '<script type="module" crossorigin src="/index-uhv_Skau.js?v=7"></script>'
replacement = '<script type="module" crossorigin src="/index-uhv_Skau.js?v=8"></script>'

if target in text:
    text = text.replace(target, replacement)
print("Cache busted index-uhv_Skau.js.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

