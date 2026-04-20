import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'and final training."})]})]}),null]})]}),e==="sync"&&'

replacement = 'and final training."})]})]}),s.jsxs("div",{className:"mt-8 pt-6 border-t border-white/10 flex justify-between items-center",children:[s.jsx("div",{className:"text-gray-400 font-mono text-sm",children:"Starting from"}),s.jsxs("div",{className:"flex gap-4 items-center",children:[s.jsx("span",{className:"text-2xl font-mono font-bold text-biometric-blue",children:"$5000"}),s.jsx("button",{onClick:()=>addSrv({id:"srv-install",name:"Installation Services",price:5000,image:"./categories/bionic.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart"})]})]})]})]}),e==="sync"&&'

if target in text:
    new_text = text.replace(target, replacement)
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced.")
else:
    print("Target not found.")

