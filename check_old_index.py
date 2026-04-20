import subprocess
import os
import io

os.chdir('..')

# Extract unmodified index-uhv_Skau.js
subprocess.run(['git', 'show', 'HEAD:index-uhv_Skau.js'], stdout=open('user-login/old_index.js', 'wb'))

with io.open('user-login/old_index.js', 'r', encoding='utf-8') as f:
    old_text = f.read()

idx = old_text.find('Visit Our Global Headquarters')
if idx != -1:
    start_idx = old_text.rfind('s.jsxs("div"', 0, idx)
    end_idx = old_text.find('B2=()', idx)
    comma_idx = old_text.rfind(',', idx, end_idx)
    
    print("ORIGINAL SURROUNDING TEXT:")
    print(old_text[max(0, start_idx-200):min(len(old_text), end_idx+100)])

