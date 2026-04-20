import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('order-confirmation')
if idx != -1:
    print("Found order-confirmation!")
    print(text[max(0, idx-500):idx+800])
else:
    print("Not found in index-uhv_Skau.js")
