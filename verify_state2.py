import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

print("Services Add to Cart - $5,000:", "Add to Cart - $5,000" in text)
print("Standard Sub Add to Cart - $199:", "Add to Cart - $199" in text)
print("Premium Sub Add to Cart - $499:", "Add to Cart - $499" in text)
print("Request Consultation missing:", "Request Consultation" not in text)
