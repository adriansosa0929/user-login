import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any occurance of children:"Request" that follows /request link
new_text = re.sub(r'(to:"/request"[^>]*?children:)"Request"', r'\1"Help"', text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced all Request links in desktop and mobile.")

