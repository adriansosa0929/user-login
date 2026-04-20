import os

target_file = '../index-uhv_Skau.js'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Just find 'Request a Consultation'
idx = content.find('Request a Consultation')

if idx == -1:
    print("Error: Could not find 'Request a Consultation'")
else:
    # Look backwards from idx for the start of the div
    # It starts with s.jsxs("div",{className:"text-center mb-8"
    start_search = 's.jsxs("div",{className:"text-center mb-8"'
    start_div_idx = content.rfind(start_search, 0, idx)
    
    if start_div_idx == -1:
        print("Error: Could not find start div")
    else:
        # We also need to remove the leading comma if it exists!
        # Let's check the character before it
        if content[start_div_idx-1] == ',':
            actual_start_idx = start_div_idx - 1
        else:
            actual_start_idx = start_div_idx
            
        print(f"Found actual_start_idx at {actual_start_idx}")
        
        # Now find the end.
        end_search = 'children:"SUBMIT REQUEST"})})})'
        end_idx = content.find(end_search, idx)
        
        if end_idx == -1:
            print("Error: Could not find end search")
        else:
            actual_end_idx = end_idx + len(end_search)
            
            # Print boundaries
            print("Block start context:", repr(content[actual_start_idx-20:actual_start_idx+50]))
            print("Block end context:", repr(content[actual_end_idx-50:actual_end_idx+20]))
            
            # Slice it out
            new_content = content[:actual_start_idx] + content[actual_end_idx:]
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("Successfully patched out the form!")
