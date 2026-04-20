import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 's.jsx("h1",{className:"text-5xl md:text-7xl font-display font-bold text-transparent bg-clip-text bg-gradient-to-r from-biometric-blue via-white to-biometric-blue drop-shadow-[0_0_20px_rgba(0,240,255,0.4)] relative z-10 leading-tight",children:"About Us"})'
replacement = 's.jsx(U.h1,{initial:{opacity:0,y:20},animate:{opacity:1,y:[0,-15,0]},transition:{opacity:{duration:.8},y:{duration:4,repeat:1/0,ease:"easeInOut"}},className:"text-5xl md:text-7xl font-display font-bold text-transparent bg-clip-text bg-gradient-to-r from-biometric-blue via-white to-biometric-blue drop-shadow-[0_0_20px_rgba(0,240,255,0.4)] relative z-10 leading-tight",children:"About Us"})'

if target in text:
    text = text.replace(target, replacement)
    print("Replaced!")
else:
    print("Target not found. Let's look closer.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

