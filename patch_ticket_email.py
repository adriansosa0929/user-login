import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = "mailto:support@kamindustries.demo"
replacement = "mailto:employee1@kamindustries.local"

if target in text:
    text = text.replace(target, replacement)
    
with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Email changed.")
