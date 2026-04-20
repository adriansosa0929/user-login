import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Subscriptions check
print("Subscribe Text?:", "children:\"Subscribe\"" in text)
print("Standard Care Price Included?:", "price:500" in text)

