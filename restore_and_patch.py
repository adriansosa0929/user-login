import subprocess
import os
import io

os.chdir('..')

# 1. Restore the file to original git state
subprocess.run(['git', 'checkout', 'index-uhv_Skau.js'])
print("Restored index-uhv_Skau.js from Git.")

with io.open('index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Add prices to cart buttons
text = text.replace('children:"Add to Cart"}', 'children:"Add to Cart - $9,900"}')
# Wait, I previously used a python script `patch_add_to_cart.py` or similar to handle multiple prices correctly?
