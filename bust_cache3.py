import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '<script src="/portal.js?v=23"></script>'
replacement = '<script src="/portal.js?v=24"></script>'

if target in text:
    text = text.replace(target, replacement)
    print("Cache busted portal.js.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

