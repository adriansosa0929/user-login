with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

# I previously mutated the file to have 'className:"hidden"'
original_mutated = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"hidden"'
modified_style = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6",style:{display:"none"}'

if original_mutated in text:
    print('Found the hidden class. Replacing with display: none...')
    text = text.replace(original_mutated, modified_style)
    with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Completed successfully!')
else:
    # What if it's the original string?
    original = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
    if original in text:
        text = text.replace(original, modified_style)
        with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
            f.write(text)
        print('Completed successfully from original!')
    else:
        print('Not found at all!')
