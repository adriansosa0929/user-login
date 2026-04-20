import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\server.py'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/api/orders')
if idx != -1:
    print("Found /api/orders in server.py")
    print(text[idx:idx+800])
else:
    print("No /api/orders in server.py")
