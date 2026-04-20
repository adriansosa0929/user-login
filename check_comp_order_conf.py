import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('r("/order-confirmation")')
# Find what component is at "/order-confirmation"
m = re.search(r'path:"/order-confirmation",element:s\.jsx\((.*?)\,', text)
if m:
    compName = m.group(1)
    print("Component for order-confirmation is:", compName)
    
    # search for where `compName` is defined
    idx2 = text.find(f'{compName}=()=>')
    if idx2 != -1:
        print(text[idx2:idx2+1000])
