import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'.{0,300}sub-standard.{0,300}', text)
if m:
    print("STANDARD AROUND:")
    print(m.group(0))

m2 = re.search(r'.{0,300}sub-plat.{0,300}', text)
if m2:
    print("PLAT AROUND:")
    print(m2.group(0))

