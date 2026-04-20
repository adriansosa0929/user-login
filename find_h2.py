import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('H2=()')
print("H2 Subscriptions:", text[idx:idx+2000])
