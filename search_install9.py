import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'children:"Add to Cart"\}\)\]\}\)\]\}\)\]\}\)\]\}\),e==="repair"&&', text)
if m:
    snippet = text[max(0, m.start()-400):m.end()]
    print(snippet)
