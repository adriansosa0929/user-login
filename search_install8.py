import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'Tissue integration, physical therapy, software calibration, and final training."\}\)\]\}\)\]\}\),null\]\}\)\]\}\),e==="sync"&&s\.jsxs', text)
if m:
    snippet = text[m.start()-200:m.end()+100]
    print("MATCHED:")
    print(snippet)
else:
    print("No match")
