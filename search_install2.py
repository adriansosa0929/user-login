import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

# find where pricing or "Add to Cart" for services is
matches = re.finditer(r'Add to Cart', text)
for m in matches:
    snippet = text[max(0, m.start()-500):m.end()+600]
    if 'install' in snippet.lower() or 'service' in snippet.lower():
        print(snippet)
        print("=========")
