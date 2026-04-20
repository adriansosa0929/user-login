import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace `./kam_` with `/kam_`
new_text = re.sub(r'"\./kam_', '"/kam_', text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced all ./kam_ with /kam_")
