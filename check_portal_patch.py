import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Can we verify the patch worked?
idx = text.find('if (localStorage.getItem(')
print("Index:", idx)
print(text[idx-200:idx+300])

