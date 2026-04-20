import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('if (confirm(\'Are you sure you want to cancel or remove this item?\')) {')
if idx != -1:
    print(text[idx-200:idx+2500])
