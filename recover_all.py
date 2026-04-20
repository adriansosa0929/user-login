import os
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Services: Replace "Request Consultation" with "Add to Cart" and hook up cart
target1 = 'onClick:()=>x("consultation"),className:"w-full mt-8 bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Request Consultation"'
repl1 = 'onClick:()=>{const e=t||[];l([...e,{id:"install-service",title:"Installation Service",price:5000,image:"/categories/bionic.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Installation Service added to cart!")},className:"w-full mt-8 bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Add to Cart - $5,000"'

target2 = 'onClick:()=>x("consultation"),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Request Consultation"'

repl2_1 = 'onClick:()=>{const e=t||[];l([...e,{id:"install-service",title:"Installation Service",price:5000,image:"/categories/bionic.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Installation Service added to cart!")},className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $5,000"'
repl2_2 = 'onClick:()=>{const e=t||[];l([...e,{id:"neural-sync",title:"Neural Interfacing Sync",price:800,image:"/categories/cerebral.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Neural Interfacing Sync added to cart!")},className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $800"'
repl2_3 = 'onClick:()=>{const e=t||[];l([...e,{id:"maint-repair",title:"Maintenance & Repair",price:500,image:"/categories/ocular.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Maintenance & Repair added to cart!")},className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $500"'

# Replace the 3 items individually
if text.count(target2) == 3:
    text = text.replace(target2, repl2_1, 1)
    text = text.replace(target2, repl2_2, 1)
    text = text.replace(target2, repl2_3, 1)

if target1 in text:
    text = text.replace(target1, repl1)

# 2. Header and Nav "Request" -> "About Us"
text = text.replace('to:"/request",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"Request"', 'to:"/contact",className:(e=>{let{isActive:t}=e;return`text-sm font-mono uppercase tracking-widest transition-colors ${t?"text-biometric-blue":"text-gray-400 hover:text-white"}`}),children:"About Us"')
text = text.replace('to:"/request",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"Request"', 'to:"/contact",onClick:e,className:(t=>{let{isActive:n}=t;return`block text-sm font-mono uppercase tracking-widest ${n?"text-biometric-blue":"text-gray-400"}`}),children:"About Us"')

# Subscription adds
target_sub1 = 'className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Subscribe"'
repl_sub1 = 'onClick:()=>{const e=t||[];l([...e,{id:"sub-standard",title:"Standard Care",price:500,image:"/categories/bionic.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Standard Care added to cart!")},className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $500"'

target_sub2 = 'className:"px-4 py-2 bg-biometric-blue text-black font-bold text-xs uppercase tracking-widest rounded hover:bg-white transition-all",children:"Subscribe"'
repl_sub2 = 'onClick:()=>{const e=t||[];l([...e,{id:"sub-gold",title:"Gold Tier",price:1200,image:"/categories/bionic.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Gold Tier added to cart!")},className:"px-4 py-2 bg-biometric-blue text-black font-bold text-xs uppercase tracking-widest rounded hover:bg-white transition-all",children:"Add to Cart - $1,200"'

target_sub3 = 'className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Subscribe"'
repl_sub3 = 'onClick:()=>{const e=t||[];l([...e,{id:"sub-plat",title:"Platinum Elite",price:2500,image:"/categories/bionic.png"}]),window.dispatchEvent(new Event("kam_cart_updated")),alert("Platinum Elite added to cart!")},className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - $2,500"'

text = text.replace(target_sub1, repl_sub1)
text = text.replace(target_sub2, repl_sub2)
text = text.replace(target_sub3, repl_sub3)

# For any remaining "Submit Request" to "About Us"? Wait, the user said "...was replaced by About Us"
# They want it to be "About Us"! My script above does that.

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied missing comprehensive patches!")
