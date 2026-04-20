import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('s.jsxs("div",{className:"bg-black/40 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group"')
idx2 = text.find(',null]}),B2=()')

if idx1 != -1 and idx2 != -1:
    new_text = text[:idx1] + "null" + text[idx2:]
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced global headquarters block manually.")
else:
    print("Failed to find boundaries.")
