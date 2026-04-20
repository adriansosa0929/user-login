import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'className:"w-full h-full object-cover', text)
if m:
    print("Found object-cover:", text[m.start()-200:m.start()+200])

m = re.search(r'img[^>]+src=', text)
if m:
    print("Found img src:", text[m.start()-200:m.start()+200])

