import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Verify Header "Request"
print("Header Request:", "children:\"Request\"" in text)
print("Header About Us:", "children:\"About Us\"" in text)

# Verify product images
print("Product Image Kam_ocular:", "kam_ocular_implant.png" in text)

# Verify services Add to Cart
print("Services Add to Cart - $5,000:", "Add to Cart - $5,000" in text)

# Verify old emails
print("Email support@kamindustries:", "support@kamindustries.demo" in text)

