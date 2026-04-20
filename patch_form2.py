import os

target_file = '../index-uhv_Skau.js'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

header = 'children:"Fill out the form below and our team will contact you within 24 hours"'
idx = content.find(header)

if idx != -1:
    start_form_idx = content.find(',s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"', idx)
    end_form_str = 'children:"SUBMIT REQUEST"})'
    end_form_idx = content.find(end_form_str, start_form_idx)
    
    if start_form_idx != -1 and end_form_idx != -1:
        end_cut = end_form_idx + len(end_form_str)
        print("FOUND! Removing form...")
        
        new_content = content[:start_form_idx] + content[end_cut:]
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Patched successfully!")
    else:
        print("Form structure not found")
else:
    print("Header not found")
