import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'o?"Processing...":"Premium Clearance"'
idx = text.find(target)
if idx != -1:
    start_idx = text.rfind('onClick:', 0, idx)
    end_idx = idx + len(target)
    
    subs_repl_premium = 'onClick:()=>{const e_ls=JSON.parse(localStorage.getItem("cart")||"[]");e_ls.push({id:"sub-premium",title:"Premium Access",price:499,image:"/categories/cerebral.png"});localStorage.setItem("cart",JSON.stringify(e_ls));window.dispatchEvent(new Event("kam_cart_updated"));alert("Premium Access added to cart!")},className:"w-full py-3 bg-neural-neon border border-neural-neon text-black hover:bg-white hover:border-white font-display font-bold rounded transition-all tracking-widest uppercase text-sm shadow-[0_0_20px_rgba(202,138,4,0.4)]",children:"Add to Cart - $499"'
    
    text = text[:start_idx] + subs_repl_premium + text[end_idx:]
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Premium Subscription Patched Successfully.")

