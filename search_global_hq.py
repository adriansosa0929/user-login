import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Global Headquarters')
if idx != -1:
    print("Found 'Global Headquarters'")
    print(text[max(0, idx-100):min(len(text), idx+500)])
else:
    print("Not found.")

