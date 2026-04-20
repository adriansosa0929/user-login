import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'Installation Process Timeline', text)
if m:
    print(text[m.start():m.end()+2500])
