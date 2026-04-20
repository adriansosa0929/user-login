import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Add to Cart - $499')
start = max(0, idx - 1000)
end = min(len(text), idx + 200)

print(text[start:end])
