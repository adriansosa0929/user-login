import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Header Nav
text = text.replace('to:"/request",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"Request"', 'to:"/contact",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"About Us"')
text = text.replace('to:"/request",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"Request"', 'to:"/contact",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"About Us"')

# Replace Submit Request
target = 'children:"Submit Request"'
replacement = 'children:"About Us"'
if target in text:
    text = text.replace(target, replacement)

# Replace Help & Support
target_help = 'children:"Help & Support"'
replacement_help = 'children:"About Us"'
if target_help in text:
    text = text.replace(target_help, replacement_help)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Bump Cache
html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=17', 'index-uhv_Skau.js?v=18')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced Request with About Us and bumped to v18.")
