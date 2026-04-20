import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Hide Global Headquarters by injecting ' hidden !important' into the outermost container
target1 = 's.jsxs("div",{className:"bg-white/5 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group"'
replacement1 = 's.jsxs("div",{className:"hidden !important bg-white/5 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group"'

if target1 in text:
    text = text.replace(target1, replacement1)
    print("Hid Global Headquarters.")

# Hide Consultation Request Form
target2 = 's.jsxs(U.form,{initial:{opacity:0},animate:{opacity:1},transition:{delay:.2},className:"bg-black/80 border border-biometric-blue rounded-2xl p-8 backdrop-blur-sm space-y-6 shadow-[0_0_30px_rgba(0,240,255,0.15)] relative overflow-hidden"'
replacement2 = 's.jsxs(U.form,{initial:{opacity:0},animate:{opacity:1},transition:{delay:.2},className:"hidden !important bg-black/80 border border-biometric-blue rounded-2xl p-8 backdrop-blur-sm space-y-6 shadow-[0_0_30px_rgba(0,240,255,0.15)] relative overflow-hidden"'

if target2 in text:
    text = text.replace(target2, replacement2)
    print("Hid Consultation Form.")


with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

