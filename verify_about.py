import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "Request" around the Nav links
# Nav links usually look like text-biometric-blue etc.
matches = re.finditer(r'children:"Request"', text)
found_request = False
for m in matches:
    found_request = True
    print("Found Request:", text[max(0, m.start()-100):min(len(text), m.end()+100)])

matches = re.finditer(r'children:"ABOUT US"', text, re.IGNORECASE)
found_about = False
for m in matches:
    found_about = True
    print("Found ABOUT US:", text[max(0, m.start()-100):min(len(text), m.end()+100)])

if not found_request:
    print("NO Request FOUND")
if not found_about:
    print("NO About Us FOUND")
