import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('D2=()=>s.jsxs(s.Fragment')
if idx == -1: idx = text.find('D2=()')

print(text[idx:idx+2000])

