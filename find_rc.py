import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all buttons containing Request Consultation
matches = re.finditer(r'\{([^}]+children:"Request Consultation"[^}]*)\}', text)
for m in matches:
    print(m.group(1))

