import re
import io

with io.open(r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js', 'r', encoding='utf-8') as f:
    text = f.read()

if 'mailto:' in text:
    print("mailto is PRESENT in portal.js")
else:
    print("mailto is MISSING from portal.js")
