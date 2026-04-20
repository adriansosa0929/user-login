import os

target_file = '../index-uhv_Skau.js'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to keep: 
# s.jsx("p",{... children:"Fill out the form below and our team will contact you within 24 hours"})]}),
# The form starts with:
form_start_str = ',s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
form_start_idx = content.find(form_start_str)

if form_start_idx == -1:
    print("Could not find start form string!")
else:
    # The submit button is:
    button_end_str = 'children:"Submit Consultation Request"})})'
    button_idx = content.find(button_end_str, form_start_idx)
    
    if button_idx == -1:
        print("Could not find button string!")
    else:
        # We need to compute where to slice.
        # Everything from form_start_idx to button_idx + len(button_end_str) will be removed.
        slice_end_idx = button_idx + len(button_end_str)
        
        # Verify
        print("Removing section starting with:", repr(content[form_start_idx:form_start_idx+60]))
        print("Ending with:", repr(content[slice_end_idx-60:slice_end_idx]))
        print("Remaining string after begins with:", repr(content[slice_end_idx:slice_end_idx+30]))
        
        new_content = content[:form_start_idx] + content[slice_end_idx:]
        
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("Patched successfully!")
