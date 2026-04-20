import re
with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

m2 = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("span",\{className:"text-purple-400 font-bold.{0,800}sub-plat.{0,500}', text)
if m2:
    print("\nPlatinum structure:\n" + m2.group(0))
else:
    print("NO PLAT FULL MATCH")

    # Let's search loosely for Plat
    m3 = re.search(r'.{0,300}Platinum.{0,300}', text[text.find('Platinum Elite"'):])
    if m3:
        print("\nLoose Plat:\n" + m3.group(0))
