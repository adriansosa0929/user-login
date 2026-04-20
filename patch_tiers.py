import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Standard
old_std = 's.jsxs("span",{className:"text-biometric-blue font-mono text-xl whitespace-nowrap",children:["$500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]})'
new_std = 's.jsxs("div",{className:"flex flex-col items-end gap-2",children:[s.jsxs("span",{className:"text-biometric-blue font-mono text-xl whitespace-nowrap",children:["$500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-standard",title:"Standard Care",price:500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $500"})]})'

if text.count(old_std) >= 1:
    text = text.replace(old_std, new_std)
    print("Patched Standard Tier")
else:
    print("Warning: Standard Tier NOT FOUND")

# 2. Gold
old_gold = 's.jsxs("span",{className:"relative z-10 text-biometric-blue font-bold font-mono text-xl whitespace-nowrap shadow-black drop-shadow-md",children:["$1,200 ",s.jsx("span",{className:"text-sm text-biometric-blue/70",children:"/yr"})]})'
new_gold = 's.jsxs("div",{className:"flex flex-col items-end gap-2 relative z-10",children:[s.jsxs("span",{className:"text-biometric-blue font-bold font-mono text-xl whitespace-nowrap shadow-black drop-shadow-md",children:["$1,200 ",s.jsx("span",{className:"text-sm text-biometric-blue/70",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-biometric-blue text-black font-bold text-xs uppercase tracking-widest rounded hover:bg-white transition-all",children:"Add to Cart - $1,200"})]})'

if text.count(old_gold) >= 1:
    text = text.replace(old_gold, new_gold)
    print("Patched Gold Tier")
else:
    print("Warning: Gold Tier NOT FOUND")

# 3. Platinum
old_plat = 's.jsxs("span",{className:"text-purple-400 font-bold font-mono text-xl whitespace-nowrap",children:["$2,500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]})'
new_plat = 's.jsxs("div",{className:"flex flex-col items-end gap-2",children:[s.jsxs("span",{className:"text-purple-400 font-bold font-mono text-xl whitespace-nowrap",children:["$2,500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-plat",title:"Platinum Elite",price:2500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - $2,500"})]})'

if text.count(old_plat) >= 1:
    text = text.replace(old_plat, new_plat)
    print("Patched Platinum Tier")
else:
    print("Warning: Platinum Tier NOT FOUND")


with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Tiers cart rewrite completed.")
