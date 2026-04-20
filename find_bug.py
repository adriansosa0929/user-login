import re
with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[.{0,600}\}\)\]\}\)', text)
if m:
    print(m.group(0))
else:
    print("Not found nested wrapper")

m2 = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[.{0,600}Add to Cart - \$500.{0,300}', text)
if m2:
    print("\nFallback print Standard:\n" + m2.group(0))
