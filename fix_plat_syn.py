import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find exactly the block starting from the outermost s.jsxs("div" that we added for plat
# and replace it up to the end of the button + ]}.
m = re.search(r'(s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[.*?children:"Add to Cart - \$2,500"\}\)\]\})', text)
if m:
    print("Found plat bug wrapper")
    matched = m.group(1)
    
    # We replace it with exactly ONE wrapper ending properly in `]})` - wait, the regex above matched `]})`! Let's check what it really is:
    # If it ends with ]} without ), we can match ]}
    m2 = re.search(r'(s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[.*?children:"Add to Cart - \$2,500"\}\)\]\}?)', text)
    if m2:
        matched2 = m2.group(1)
        print("M2 matched exact block:\n" + matched2[:100] + "..." + matched2[-50:])
        correct_plat = 's.jsxs("div",{className:"flex flex-col items-end gap-2",children:[s.jsxs("span",{className:"text-purple-400 font-bold font-mono text-xl whitespace-nowrap",children:["$2,500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-plat",title:"Platinum Elite",name:"Platinum Elite",price:2500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - $2,500"})]})'
        
        text = text.replace(matched2, correct_plat)
        
        with io.open(file_path, 'w', encoding='utf-8') as fw:
            fw.write(text)
        print("Replaced Platinum!")
    else:
        print("m2 not found")
else:
    print("m1 not found")

