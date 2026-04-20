import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Current Gold
current_gold = 's.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"};'

# Target Gold
target_gold = 's.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"};'

if current_gold in text:
    text = text.replace(current_gold, target_gold)
    print("Gold Tier propagation stopped.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done.")
