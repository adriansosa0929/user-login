import re
import io
import os
import shutil

# First, let's restore the original file from the previous backup if possible.
# Actually, I didn't make a formal backup of index-uhv_Skau.js.
# BUT I can fetch the file content, find where `B2=()` starts, and look at the preceding characters to see the damage.
file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('B2=()')
if idx != -1:
    print(text[max(0, idx-500):min(len(text), idx+100)])

