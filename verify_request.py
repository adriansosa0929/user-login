import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

count = len(re.findall(r'(?i)children:"Request"', text))
print("Remaining occurrences of children:'Request':", count)
