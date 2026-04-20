import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find the exact block for "Global Headquarters"
# We know it starts with `s.jsxs("div",{className:"bg-black/40 border border-white/10 rounded-2xl`
# and ends right before `,null]}),B2=()`

idx1 = text.find('s.jsxs("div",{className:"bg-black/40 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group"')
idx2 = text.find('B2=()=>s.jsxs("div",{className:"max-w-6xl mx-auto p-4"')

if idx1 != -1 and idx2 != -1:
    old_block = text[idx1:idx2]
    print("Found block to remove:")
    print(old_block[:100] + "..." + old_block[-100:])
    
    # Wait, if we just remove the `s.jsxs` block, what is the preceding character?
    # It might be `,[s.jsxs("div", ...)]}),B2=()`
    
    # Since we don't know the exact syntax tree around it, let's carefully replace the visible block 
    # with `null` so React just renders nothing.
    
    new_text = text[:idx1] + "null" + text[idx2-len(',null]}),'):]
    
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced with null!")

