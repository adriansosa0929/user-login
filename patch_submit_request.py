import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'children:"Submit Request"'
replacement = 'children:"About Us"'

if target in text:
    text = text.replace(target, replacement)
    print("Replaced.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

