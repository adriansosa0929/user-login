import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

new_text = re.sub(r'(to:"/request"[^>]*?children:)"Help"', r'\1"About Us"', text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("regex replace executed")
