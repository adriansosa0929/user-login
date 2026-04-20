import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the specific div with an empty element
target = r's\.jsxs\("div",\{className:"bg-black/40 border border-white/10 rounded-2xl p-8 md:p-12 relative overflow-hidden text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 group",children:.*?\}\)\}\)\}\]\}\)'

def repl(m):
    return 'null'

new_text = re.sub(target, repl, text, flags=re.DOTALL)

if new_text != text:
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced global headquarters block using regex.")
else:
    print("Regex failed to match.")
