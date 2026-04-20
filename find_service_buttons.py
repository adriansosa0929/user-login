import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for the exact button in products/services page
# It should be px-6 py-2 bg-biometric-blue
matches = re.findall(r'className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"[^"]+"', text)
print("Found buttons:")
for m in matches:
    print(m)

# Let's see what is onClick before it
matches = re.finditer(r'onClick:[^,]+,className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"[^"]+"', text)
for m in matches:
    print(m.group(0))

