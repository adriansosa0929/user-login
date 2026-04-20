import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# I want to specifically replace the `children:"Help"` occurrences that belong to the nav links.
# The mobile: 'border-white text-white font-bold py-4 rounded-lg uppercase tracking-widest transition-all text-center",children:"Help"})'
# The desktop: 'text-gray-400"}`,children:"Help"})'

desktop_target = '`/request"?"text-emerald-400":"text-gray-400"}`,children:"Help"})'
desktop_replacement = '`/request"?"text-emerald-400":"text-gray-400"}`,children:"About Us"})'

mobile_target = 'text-center",children:"Help"})]})]}'
mobile_replacement = 'text-center",children:"About Us"})]})]}'


if desktop_target in text:
    text = text.replace(desktop_target, desktop_replacement)
    print("Desktop link replaced.")

if mobile_target in text:
    text = text.replace(mobile_target, mobile_replacement)
    print("Mobile link replaced.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

