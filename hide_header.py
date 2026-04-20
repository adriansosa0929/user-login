with open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

original = 's.jsx("h2",{className:"text-2xl font-display font-bold text-white mb-2",children:"Request a Consultation"})'

if original in text:
    text = text.replace(original, 'null')
    with open('../index-uhv_Skau.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Header successfully removed!')
else:
    print('Original not found.')
