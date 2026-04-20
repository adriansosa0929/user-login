import re
import io
import json

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# First, extract everything inside `products:[...]` blocks
product_blocks = re.findall(r'products:\[(.*?)\]\}\}', text)
for block in product_blocks:
    # Within each block, parse each object by finding {id:...}
    matches = re.finditer(r'\{id:"([^"]+)",name:"([^"]+)"[^}]+description:"([^"]+)"\}', block)
    for m in matches:
        print(f"ID: {m.group(1)}")
        print(f"Name: {m.group(2)}")
        print(f"Desc: {m.group(3)}")
        print("=========")
