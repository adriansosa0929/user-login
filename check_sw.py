import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

if 'serviceWorker' in text:
    print("Found serviceWorker registration!")
else:
    print("No serviceWorker registered in index.html.")

