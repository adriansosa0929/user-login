import io

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Target 1: Maintenance tab Schedule Repair button -> Add to Cart
old_maint_btn = 's.jsx(V,{to:"/request",className:"w-full block text-center bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Schedule Repair"})'

new_maint_btn = 's.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"maint-repair",title:"Maintenance & Repair",price:500,image:"/categories/ocular.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"w-full block text-center bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Add to Cart - $500"})'

if old_maint_btn in text:
    text = text.replace(old_maint_btn, new_maint_btn)
    print("Successfully patched Maintenance tab button!")
else:
    print("Warning: Could not find Maintenance tab button to patch.")

# Target 2: Homepage/Services bottom 3 Ln cards
# A) Installation
old_install_ln = 's.jsx(Ln,{title:"Installation Services",description:"Professional surgical implementation by certified cyber-surgeons in sterile facilities.",icon:Vp,to:"/services",color:"text-orange-400",delay:0})'
new_install_ln = 's.jsxs("div",{className:"flex flex-col gap-4",children:[' + old_install_ln + ',s.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"install-service",title:"Installation Service",price:5000,image:"/categories/bionic.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"w-full px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $5,000"})]})'

if old_install_ln in text:
    text = text.replace(old_install_ln, new_install_ln)
    print("Successfully patched Installation Ln!")
else:
    print("Warning: Could not find Installation Ln.")

# B) Neural Interfacing
old_sync_ln = 's.jsx(Ln,{title:"Neural Interfacing",description:"Precise calibration and synchronization of your biological and synthetic nervous systems.",icon:hi,to:"/services",color:"text-biometric-blue",delay:.1})'
new_sync_ln = 's.jsxs("div",{className:"flex flex-col gap-4",children:[' + old_sync_ln + ',s.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"neural-sync",title:"Neural Interfacing Sync",price:800,image:"/categories/cerebral.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"w-full px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $800"})]})'

if old_sync_ln in text:
    text = text.replace(old_sync_ln, new_sync_ln)
    print("Successfully patched Neural Interfacing Ln!")
else:
    print("Warning: Could not find Neural Interfacing Ln.")

# C) Maintenance
old_maint_ln = 's.jsx(Ln,{title:"Maintenance & Repair",description:"24/7 diagnostic monitoring, regular tune-ups, and emergency repair services.",icon:Bp,to:"/services",color:"text-green-400",delay:.2})'
new_maint_ln = 's.jsxs("div",{className:"flex flex-col gap-4",children:[' + old_maint_ln + ',s.jsx("button",{onClick:()=>{const currentCartStr=localStorage.getItem("cart")||"[]";let currentCart=[];try{currentCart=JSON.parse(currentCartStr);}catch(err){}let item={id:"maint-repair",title:"Maintenance & Repair",price:500,image:"/categories/ocular.png"};currentCart.push(item);localStorage.setItem("cart",JSON.stringify(currentCart));window.dispatchEvent(new Event("kam_cart_updated"));alert(item.title+" added to cart!");window.location.hash="#/cart";},className:"w-full px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $500"})]})'

if old_maint_ln in text:
    text = text.replace(old_maint_ln, new_maint_ln)
    print("Successfully patched Maintenance & Repair Ln!")
else:
    print("Warning: Could not find Maintenance & Repair Ln.")

# Save modifications
with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished applying all cart patches.")
