import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Verify main product add to cart
print("Main Product Add to Cart format present?", "children:`Add to Cart - $$" in text)
