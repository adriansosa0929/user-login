import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Search for the About Us heading
m = re.search(r'children:"About Us"', text)
if m:
    print("Found About Us:", text[max(0, m.start()-300):min(len(text), m.end()+300)])
