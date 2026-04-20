import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

print("Original watcher logic:")
idx = text.find('// If cart emptied, snapshot it into persistent history')
if idx != -1:
    print(text[idx:idx+800])
