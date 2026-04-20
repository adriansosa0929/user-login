import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# The user wants to replace "Request" at the top with "Help".
# This likely refers to the desktop and mobile navigation links.
# They are both defined via `children:"Request"` where the link is `/request`.

# Replace the specific instances:
desktop_target = '`/request"?"text-emerald-400":"text-gray-400"}`,children:"Request"})'
desktop_replacement = '`/request"?"text-emerald-400":"text-gray-400"}`,children:"Help"})'

mobile_target = 'text-center",children:"Request"})]})]}'
mobile_replacement = 'text-center",children:"Help"})]})]}'


if desktop_target in text:
    text = text.replace(desktop_target, desktop_replacement)
    print("Desktop link replaced.")

if mobile_target in text:
    text = text.replace(mobile_target, mobile_replacement)
    print("Mobile link replaced.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

