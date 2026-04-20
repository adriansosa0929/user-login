import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('element:s.jsx(U2')
if idx != -1:
    print("Found U2 usage:")
    print(text[max(0, idx-100):idx+200])

idx = text.find('element:s.jsx(B2')
if idx != -1:
    print("Found B2 usage:")
    print(text[max(0, idx-100):idx+200])

