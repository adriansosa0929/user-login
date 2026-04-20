import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# search for image tags
m = re.finditer(r'<img[^>]+src=[^>]+>', text)
for match in m:
    print(match.group(0))
    print()

# search for src=" something "
m = re.finditer(r'src:"[^"]+"', text)
for match in m:
    print(match.group(0))
    
