import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

target = 'and final training."})]})]}),null]})]}),e==="sync"&&'
if target in text:
    print("Found! Count:", text.count(target))
else:
    print("Not found.")
