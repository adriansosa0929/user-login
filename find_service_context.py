import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for Neural Link v2 or Installation Service
matches = re.finditer(r'\{([^}]+children:"Installation Service"[^}]*)\}', text)
for m in matches:
    print(m.group(1))

# Search for the button next to Installation Service
idx = text.find('Installation Service')
if idx != -1:
    print("\nSurrounding context:")
    print(text[max(0, idx-50):min(len(text), idx+500)])
