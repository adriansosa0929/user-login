import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Request nav links
text = re.sub(r'children:"Request"\}', r'children:"ABOUT US"}', text)

# Replace Submit Request
text = text.replace('children:"Submit Request"', 'children:"ABOUT US"')

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Bump Cache
html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=18', 'index-uhv_Skau.js?v=19')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced Request nav & Submit Request to ABOUT US. Bumped to v19.")
