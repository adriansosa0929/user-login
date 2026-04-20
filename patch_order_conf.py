import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'confirm("Are you sure you want to cancel this order and request a refund?")&&(i(!0),alert("Refund request submitted successfully! Funds will return to your account in 3-5 business days."))'

replacement = 'confirm("Are you sure you want to cancel this order and request a refund?")&&(i(!0), (()=>{try{let h=JSON.parse(localStorage.getItem("kam_orders")||"[]");h.pop();localStorage.setItem("kam_orders",JSON.stringify(h));if(window.renderOrders)window.renderOrders();}catch(e){}})(),alert("Refund request submitted successfully! Funds will return to your account in 3-5 business days."))'

if target in text:
    text = text.replace(target, replacement)
    print("Replaced order confirmation cancel logic!")
else:
    print("WARNING: target not found")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

