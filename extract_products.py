import re
import json

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We need to extract the product objects.
# We can use regular expressions to find all {id:"...",name:"...",price:...,image:"...",specs:{...},description:"..."}
# Wait, this regex will be robust enough.
pattern = r'\{id:"([^"]+)",name:"([^"]+)",[^{]*image:"([^"]+)"[^}]*description:"([^"]+)"\}'
matches = re.finditer(pattern, text)

products = []
for m in matches:
    product = {
        "id": m.group(1),
        "name": m.group(2),
        "image": m.group(3),
        "description": m.group(4)
    }
    products.append(product)

import pprint
for p in products:
    print(f"ID: {p['id']}, Name: {p['name']}, Desc: {p['description']}")
