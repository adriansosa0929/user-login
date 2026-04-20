import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("div",\{className:"flex flex-col items-end gap-2".{0,800}', text)
if m:
    print("STANDARD MATCH:")
    print(m.group(0))

m2 = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("div",\{className:"flex flex-col items-end gap-2".{0,800}', text[m.end() if m else 0:])
if m2:
    print("PLATINUM MATCH:")
    print(m2.group(0))
    
m3 = re.search(r's\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[.{0,1000}', text[text.find('Platinum Elite'):])
if m3:
    print("ALL PLAT:")
    print(m3.group(0))

