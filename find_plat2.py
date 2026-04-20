import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'.{0,400}Add to Cart - \$2,500.{0,300}', text)
if m:
    print("PLAT AROUND:\n" + m.group(0))

