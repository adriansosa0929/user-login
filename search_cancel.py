import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

cancel_matches = re.finditer(r'cancel|return', text, re.IGNORECASE)
for m in cancel_matches:
    print("Match around:", m.start())
    print(text[max(0, m.start() - 100):min(len(text), m.end() + 200)])
    print("===")
