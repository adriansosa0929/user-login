import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Change Header back to "Request"
text = text.replace('to:"/contact",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"About Us"', 'to:"/request",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"Request"')
text = text.replace('to:"/contact",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"About Us"', 'to:"/request",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"Request"')

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Also ensure index.html cache is busted for both
html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=13', 'index-uhv_Skau.js?v=14')
html = html.replace('portal.js', 'portal.js?v=14')
# If it already had v=, it will just append, which is fine e.g. portal.js?v=25?v=14 (browser will cache bust). But let's be cleaner.
import re
html = re.sub(r'portal.js(\?v=\d+)?', r'portal.js?v=15', html)

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Reverted About Us to Request and bumped cache!")
