target_file = '../index-uhv_Skau.js'
with open(target_file, 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('contact you within 24 hours')
if idx != -1:
    with open('form.txt', 'w', encoding='utf-8') as out:
        out.write(c[idx:idx+4000])
