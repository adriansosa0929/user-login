import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = "if (typeof openKamPortal === 'function') openKamPortal('orders');"
replacement = "if (typeof window.openKamPortal === 'function') window.openKamPortal('orders');"

text = text.replace(target, replacement)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated openKamPortal check.")
