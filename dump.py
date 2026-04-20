target_file = '../index-uhv_Skau.js'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.find('contact you within 24 hours')
with open('form_dump.txt', 'w', encoding='utf-8') as out:
    out.write(content[max(0, idx-100):idx+3000])
