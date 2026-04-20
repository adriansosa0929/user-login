import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\user-login\remove_hq_safe.py'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
print(text)
