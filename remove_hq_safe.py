import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('Visit Our Global Headquarters')
if idx1 != -1:
    # Find the nearest s.jsxs("div" before this
    start_idx = text.rfind('s.jsxs("div"', 0, idx1)
    # Find the nearest B2=() after this to know where it ends exactly
    end_idx = text.find('B2=()', idx1)
    
    if start_idx != -1 and end_idx != -1:
        # We need to backtrack from B2=() to the preceding comma
        comma_idx = text.rfind(',', idx1, end_idx)
        print("Slice between", start_idx, "and", comma_idx)
        print(text[start_idx:comma_idx+1])
        new_text = text[:start_idx] + "null" + text[comma_idx:]
        
        with io.open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Replaced global headquarters block.")
    else:
        print("Could not find boundaries around Visit Our Global Headquarters")
