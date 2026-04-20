import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Gold Tier "View Subscription Plans"
target1 = 's.jsx(V,{to:"/subscribe",className:"w-full inline-block bg-biometric-blue hover:bg-white text-black font-bold py-3 text-sm rounded transition-all uppercase tracking-wider",children:"View Subscription Plans"})'
repl1 = 's.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr)}catch(err){}const item={id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!")},className:"w-full inline-block bg-biometric-blue hover:bg-white text-black font-bold py-3 text-sm rounded transition-all uppercase tracking-wider",children:"Add to Cart - $1,200"})'

# Replace Platinum Elite "View Subscription Plans"
target2 = 's.jsx(V,{to:"/subscribe",className:"w-full inline-block bg-purple-500 hover:bg-purple-400 text-white font-bold py-3 text-sm rounded transition-all uppercase tracking-wider shadow-[0_0_15px_rgba(168,85,247,0.4)]",children:"View Subscription Plans"})'
repl2 = 's.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr)}catch(err){}const item={id:"sub-plat",title:"Platinum Elite",price:2500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!")},className:"w-full inline-block bg-purple-500 hover:bg-purple-400 text-white font-bold py-3 text-sm rounded transition-all uppercase tracking-wider shadow-[0_0_15px_rgba(168,85,247,0.4)]",children:"Add to Cart - $2,500"})'

if target1 in text:
    text = text.replace(target1, repl1)
    print("Gold patched")
if target2 in text:
    text = text.replace(target2, repl2)
    print("Platinum patched")

if target2 not in text:
    # Just let me know if it failed so I can use regex
    print("T2 not found exactly.")


with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Bump Cache
html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=20', 'index-uhv_Skau.js?v=21')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
