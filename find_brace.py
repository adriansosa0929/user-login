def find_matching_bracket(text, start_index):
    count = 0
    in_str = False
    escape = False
    str_char = ''
    for i in range(start_index, len(text)):
        c = text[i]
        
        if escape:
            escape = False
            continue
            
        if c == '\\':
            escape = True
            continue
            
        if in_str:
            if c == str_char:
                in_str = False
            continue
            
        if c in ('"', "'", '`'):
            in_str = True
            str_char = c
            continue
            
        if c == '[': count += 1
        elif c == ']':
            count -= 1
            if count == 0:
                return i
    return -1

with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

# First, restore the original string from my last test if we modified it
modified_style = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6",style:{display:"none"}'
original = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
if modified_style in text:
    text = text.replace(modified_style, original)

idx = text.find(original)
if idx == -1:
    print("Could not find the original string.")
else:
    # Find the children array bracket specifically:
    # original ends with `gap-6"`
    # next is `,children:[`
    # Let's search for `,children:[` starting from idx
    children_idx = text.find(',children:[', idx)
    if children_idx != -1:
        bracket_start = children_idx + len(',children:')
        # bracket_start points to '['
        bracket_end = find_matching_bracket(text, bracket_start)
        
        if bracket_end != -1:
            print("Found form array from", bracket_start, "to", bracket_end)
            # The form is the div container: s.jsxs("div",{... children: [...] })
            # If we just replace [...] with [] it deletes the form fields completely!
            old_form_children = text[bracket_start:bracket_end+1]
            new_text = text[:bracket_start] + '[]' + text[bracket_end+1:]
            with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
                f.write(new_text)
            print("Successfully emptied the form array!")
        else:
            print("Could not balance brackets.")
    else:
        print("Could not find children:[")
