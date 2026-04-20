import re

with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

# I will find the EXACT string block that is messed up by looking at where the double s.jsxs("div" ... flex column starts.
# Standard:
m = re.search(r'(s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("span",\{className:"text-biometric-blue font-mono text-xl whitespace-nowrap",children:\["\$500 ",s\.jsx\("span",\{className:"text-sm text-gray-500",children:"/yr"\}\)\]\}\),s\.jsx\("button",\{onClick:\(e\)=>\{e\.stopPropagation\(\);const currentCartStr=localStorage\.getItem\("cart"\)\|\|"\[\]";let currentCart=\[\];try\{currentCart=JSON\.parse\(currentCartStr\);\}catch\(err\)\{\}let item=\{id:"sub-standard",title:"Standard Care",name:"Standard Care",price:500,image:"/categories/bionic\.png"\};currentCart\.push\(item\);localStorage\.setItem\("cart",JSON\.stringify\(currentCart\)\);window\.dispatchEvent\(new Event\("kam_cart_updated"\)\);alert\(item\.title\+" added to cart!"\);window\.location\.hash="#/cart";\},className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - \$500"\}\)\]\}(\]{0,4}\}{1,4}\)?)+)', text)

if m:
    matched_str = m.group(1)
    print("MATCHED STANDARD STRING:\n", matched_str[:200], '...', matched_str[-50:])
    # The correct replacement:
    correct_std = 's.jsxs("div",{className:"flex flex-col items-end gap-2",children:[s.jsxs("span",{className:"text-biometric-blue font-mono text-xl whitespace-nowrap",children:["$500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-standard",title:"Standard Care",name:"Standard Care",price:500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $500"})]})'
    text = text.replace(matched_str, correct_std)

m2 = re.search(r'(s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("div",\{className:"flex flex-col items-end gap-2",children:\[s\.jsxs\("span",\{className:"text-purple-400 font-bold font-mono text-xl whitespace-nowrap",children:\["\$2,500 ",s\.jsx\("span",\{className:"text-sm text-gray-500",children:"/yr"\}\)\]\}\),s\.jsx\("button",\{onClick:\(e\)=>\{e\.stopPropagation\(\);const currentCartStr=localStorage\.getItem\("cart"\)\|\|"\[\]";let currentCart=\[\];try\{currentCart=JSON\.parse\(currentCartStr\);\}catch\(err\)\{\}let item=\{id:"sub-plat",title:"Platinum Elite",name:"Platinum Elite",price:2500,image:"/categories/bionic\.png"\};currentCart\.push\(item\);localStorage\.setItem\("cart",JSON\.stringify\(currentCart\)\);window\.dispatchEvent\(new Event\("kam_cart_updated"\)\);alert\(item\.title\+" added to cart!"\);window\.location\.hash="#/cart";\},className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - \$2,500"\}\)\]\}(\]{0,4}\}{1,4}\)?)+)', text)

if m2:
    matched_str2 = m2.group(1)
    print("MATCHED PLATINUM STRING:\n", matched_str2[:200], '...', matched_str2[-50:])
    # The correct replacement:
    correct_plat = 's.jsxs("div",{className:"flex flex-col items-end gap-2",children:[s.jsxs("span",{className:"text-purple-400 font-bold font-mono text-xl whitespace-nowrap",children:["$2,500 ",s.jsx("span",{className:"text-sm text-gray-500",children:"/yr"})]}),s.jsx("button",{onClick:(e)=>{e.stopPropagation();const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"sub-plat",title:"Platinum Elite",name:"Platinum Elite",price:2500,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - $2,500"})]})'
    text = text.replace(matched_str2, correct_plat)


with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
    f.write(text)

