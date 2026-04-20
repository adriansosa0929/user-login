import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# See if there's a React effect that saves cart
idx = text.find('localStorage.setItem("cart"')
if idx != -1:
    print("Found cart setItem in React:")
    print(text[max(0, idx-300):idx+300])
