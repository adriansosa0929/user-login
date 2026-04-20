import re
with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'bg-purple-500/10.{0,800}', text)
if m:
    print(m.group(0))
else:
    print("NOT FOUND")
