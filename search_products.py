import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for names of these products since we know they exist. 
# They are likely matching the images: kam_bionic_arm, kam_cerebral_chip, kam_ocular_implant.
m = re.finditer(r'(?i)bionic|ocular|cerebral', text)
output = []
for match in m:
    output.append(text[max(0, match.start()-100):min(len(text), match.end()+150)])

# print the unique contexts
for o in list(set(output))[:10]:
    print(o)
    print("-----")
