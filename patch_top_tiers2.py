import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Platinum Elite "View Subscription Plans" using Regex
repl2 = 's.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr)}catch(err){}const item={id:"sub-plat",title:"Platinum Elite",price:2500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!")},className:"w-full inline-block bg-purple-500 hover:bg-purple-400 text-white font-bold py-3 text-sm rounded transition-all uppercase tracking-wider shadow-[0_0_15px_rgba(168,85,247,0.4)] text-center",children:"Add to Cart - $2,500"})'

text = re.sub(r's\.jsx\(V,\{to:"/subscribe",className:"(?:[^"]+)bg-purple-50(?:[^"]+)",children:"View Subscription Plans"\}\)', repl2, text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Platinum Elite patched with regex.")
