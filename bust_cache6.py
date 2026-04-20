import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('index-uhv_Skau.js?v=9', 'index-uhv_Skau.js?v=10')

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Cache busted minified JS again.")
