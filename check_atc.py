import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'bg-blue-400 text-black font-bold py-4', text)
if m:
    print(text[m.start()-500:m.start()+500].encode('ascii', errors='ignore').decode())

