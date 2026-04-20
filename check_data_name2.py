import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('el.className = "kam-order-card";')
if idx == -1:
    idx = text.find('el.className = \'kam-order-card\';')

print("Found index:", idx)
if idx != -1:
    print(text[idx:idx+800])
