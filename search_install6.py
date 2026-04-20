import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'e==="sync"&&', text)
if m:
    snippet = text[m.start()-300:m.start()]
    print(snippet)
