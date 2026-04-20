import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/api/orders')
if idx != -1:
    print("React calls /api/orders")
else:
    print("React DOES NOT call /api/orders")

idx2 = text.find('/api/return')
if idx2 != -1:
    print("React calls /api/return")
else:
    print("React DOES NOT call /api/return")

