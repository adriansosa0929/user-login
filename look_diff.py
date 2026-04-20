import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\user-login\diff.txt'
with io.open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

idx = text.find('Global Headquarters')
print(text[max(0, idx-500):idx+500])
