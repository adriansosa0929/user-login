import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 's.jsxs("div",{className:"bg-white/5 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group",children:[s.jsx("div",{className:"absolute top-0 right-0 w-64 h-64 bg-biometric-blue/10 blur-[80px] rounded-full pointer-events-none group-hover:bg-biometric-blue/20 transition-colors"}),null,B2='

replacement = 'null]}),B2='

if target in text:
    text = text.replace(target, replacement)
    print("Fixed syntax error!")
else:
    print("WARNING: target not found.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

