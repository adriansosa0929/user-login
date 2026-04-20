import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('ticket')
if idx != -1:
    print("Found 'ticket' at", idx)
    print(text[max(0, idx-100):min(len(text), idx+100)])

# Look for form IDs
import re
forms = re.findall(r'<form[^>]*>', text)
print("Forms found:", forms)
