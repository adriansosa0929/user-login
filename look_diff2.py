import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\user-login\diff.txt'
with io.open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

idx = text.find('Global Headquarters')
if idx != -1:
    # Go backwards to start of diff block
    start_diff = text.rfind('@@', 0, idx)
    end_diff = text.find('@@', idx)
    if end_diff == -1: end_diff = len(text)
    
    print(text[start_diff:start_diff+1000])

