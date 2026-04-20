import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Patch Services dynamically (D2 component)
# Target is the V link component at the bottom of D2
services_target = 's.jsx(V,{to:"/request",className:"w-full block text-center bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Request Consultation"})'
services_button_logic = '''s.jsx("button",{onClick:()=>{
    const currentCartStr = localStorage.getItem("cart") || "[]";
    let currentCart = [];
    try { currentCart = JSON.parse(currentCartStr); } catch(err){}
    let item = null;
    if(e==="install") item = {id:"install-service",title:"Installation Service",price:5000,image:"/categories/bionic.png"};
    if(e==="sync") item = {id:"neural-sync",title:"Neural Interfacing Sync",price:800,image:"/categories/cerebral.png"};
    if(e==="repair") item = {id:"maint-repair",title:"Maintenance & Repair",price:500,image:"/categories/ocular.png"};
    if(e==="gold") item = {id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"};
    if(e==="platinum") item = {id:"sub-plat",title:"Platinum Elite",price:2500,image:"/categories/bionic.png"};
    if(item) {
        currentCart.push(item);
        localStorage.setItem("cart", JSON.stringify(currentCart));
        window.dispatchEvent(new Event("kam_cart_updated"));
        alert(item.title + " added to cart!");
    }
  },className:"w-full block text-center bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:`Add to Cart - $${e==="install"?"5,000":e==="sync"?"800":e==="repair"?"500":e==="gold"?"1,200":"2,500"}`})'''

# Since JavaScript strings can't use line breaks easily inside the single-line minified file, we'll strip them to space
services_button_logic = services_button_logic.replace('\n', ' ')

if services_target in text:
    text = text.replace(services_target, services_button_logic)
    print("Services Cart Patched!")

# 2. Patch Subscriptions (H2 component)
subs_target_standard = 'onClick:()=>l("standard"),disabled:!r||o,className:"w-full py-3 bg-biometric-blue/20 text-biometric-blue hover:bg-biometric-blue hover:text-black font-display font-bold rounded transition-all uppercase tracking-widest disabled:opacity-50 disabled:cursor-not-allowed text-sm",children:o?"Processing...":"Standard Clearance"'
subs_repl_standard = 'onClick:()=>{const e_ls=JSON.parse(localStorage.getItem("cart")||"[]");e_ls.push({id:"sub-standard",title:"Standard Care",price:500,image:"/categories/bionic.png"});localStorage.setItem("cart",JSON.stringify(e_ls));window.dispatchEvent(new Event("kam_cart_updated"));alert("Standard Care added to cart!")},className:"w-full py-3 bg-biometric-blue/20 text-biometric-blue hover:bg-biometric-blue hover:text-black font-display font-bold rounded transition-all uppercase tracking-widest text-sm",children:"Add to Cart - $199"'

subs_target_premium = 'onClick:()=>l("premium"),disabled:!r||o,className:"w-full py-3 bg-neural-neon border border-neural-neon text-black hover:bg-white hover:border-white font-display font-bold rounded transition-all tracking-widest uppercase disabled:opacity-50 disabled:cursor-not-allowed text-sm shadow-[0_0_20px_rgba(202,138,4,0.4)]",children:o?"Processing...":"Premium Clearance"'
subs_repl_premium = 'onClick:()=>{const e_ls=JSON.parse(localStorage.getItem("cart")||"[]");e_ls.push({id:"sub-premium",title:"Premium Access",price:499,image:"/categories/cerebral.png"});localStorage.setItem("cart",JSON.stringify(e_ls));window.dispatchEvent(new Event("kam_cart_updated"));alert("Premium Access added to cart!")},className:"w-full py-3 bg-neural-neon border border-neural-neon text-black hover:bg-white hover:border-white font-display font-bold rounded transition-all tracking-widest uppercase text-sm shadow-[0_0_20px_rgba(202,138,4,0.4)]",children:"Add to Cart - $499"'

if subs_target_standard in text:
    text = text.replace(subs_target_standard, subs_repl_standard)
    print("Standard Subscription Patched!")

if subs_target_premium in text:
    text = text.replace(subs_target_premium, subs_repl_premium)
    print("Premium Subscription Patched!")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("All Cart integration injected.")
