import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace relative paths with absolute paths from root
text = text.replace('./kam_ocular_implant.png', '/kam_ocular_implant.png')
text = text.replace('./kam_bionic_arm.png', '/kam_bionic_arm.png')
text = text.replace('./kam_cerebral_chip.png', '/kam_cerebral_chip.png')

# Also double check if there are any other relative paths
print("Ocular fixed:", "/kam_ocular_implant.png" in text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Bump Cache
html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=19', 'index-uhv_Skau.js?v=20')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Product images paths fixed to absolute and bumped to v20.")
