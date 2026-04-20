import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.finditer(r'(?i)Submit a Request', text)
for match in m:
    print("Match at:", match.start())
    print(text[max(0, match.start()-100):min(len(text), match.end()+100)])

