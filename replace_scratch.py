with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

original = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
modified = 'contact you within 24 hours"})]}),s.jsxs("div",{className:"hidden"'

if original in text:
    print('Found the original string! Modifying...')
    new_text = text.replace(original, modified)
    with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Safely removed request form!')
else:
    print('Original not found.')
