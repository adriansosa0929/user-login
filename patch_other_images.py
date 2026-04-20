import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace `./logo-` with `/logo-`
text = re.sub(r'"\./logo-', '"/logo-', text)

# Replace `./categories/` with `/categories/`
text = re.sub(r'"\./categories/', '"/categories/', text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replaced all relative image paths with absolute paths.")
