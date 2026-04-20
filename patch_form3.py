import os

target_file = '../index-uhv_Skau.js'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the heading block
info_end_str = 'contact you within 24 hours"})]}),'
info_end_idx = content.find(info_end_str)

if info_end_idx == -1:
    print("Could not find info end string")
else:
    # We want to remove everything from the comma that follows the info div,
    # up to the end of the submit button.
    start_remove_idx = info_end_idx + len('contact you within 24 hours"})]})')
    # wait, the string is '... hours"})]}),'
    # 'contact you within 24 hours"})]})' is exactly 33 chars.
    
    # Let's find the comma exactly:
    form_start_str = ',s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
    form_start_idx = content.find(form_start_str, info_end_idx)
    
    if form_start_idx == -1:
        print("Could not find form start string")
    else:
        # Find the submit button end
        button_end_str = 'children:"SUBMIT REQUEST"})'
        button_end_idx = content.find(button_end_str, form_start_idx)
        
        if button_end_idx == -1:
            print("Could not find button end string")
        else:
            remove_end_idx = button_end_idx + len(button_end_str)
            
            print("To replace:", repr(content[form_start_idx:form_start_idx+60]))
            print("To remove end:", repr(content[remove_end_idx-60:remove_end_idx+30]))
            
            new_content = content[:form_start_idx] + content[remove_end_idx:]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Patched completely!")
