import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.finditer(r'document\.addEventListener\(\'click\'', text)
for match in m:
    print("Found listener at:", match.start())
    print(text[match.start():match.start()+200])
    
m2 = re.finditer(r'kam-btn-return', text)
for match in m2:
    print("Found kam-btn-return at:", match.start())
