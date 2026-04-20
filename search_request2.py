import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

m = re.finditer(r'(?i)children:"Request"', text)
for match in m:
    print("MATCH AT", match.start())
    print(text[max(0, match.start()-150):min(len(text), match.end()+100)])
    print("---------------------------------")
