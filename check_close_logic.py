import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Search for the close logic
idx = text.find('// Close logic')
if idx == -1:
    idx = text.find('.kam-close')

if idx != -1:
    print(text[max(0, idx-200):idx+800])
