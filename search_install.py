import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'e==="install"&&"Installation Services"', text)
if m:
    print(text[m.start()-400:m.end()+1500])
else:
    print("Not found")
