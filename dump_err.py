import re

with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'.{0,300}sub-standard.{0,800}', text)
if m:
    print(m.group(0))
else:
    print("Not found")

m2 = re.search(r'.{0,300}sub-plat.{0,800}', text[m.end() if m else 0:])
if m2:
    print("\n---\n" + m2.group(0))
else:
    print("plat not found")
