import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Search for the string "Clearance" in the Subscriptions page
matches = re.finditer(r'Clearance[^\n]{0,200}', text, re.IGNORECASE)
for m in matches:
    print(m.group(0))

print("--------------")
matches = re.finditer(r'className:"text-xl font-bold mb-2[^>]*>([^<]+)</h2>', text)
for m in matches:
    print(m.group(0))

