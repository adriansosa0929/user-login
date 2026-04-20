import io

with io.open('../index-uhv_Skau.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Add to Cart - ' + chr(36) + '2,500')
if idx != -1:
    print("NEW FILE:")
    print(text[idx-50:idx+150])

with io.open('old_index.js', 'r', encoding='utf-8') as f:
    old_text = f.read()

idx_old = old_text.find('Platinum Elite')
if idx_old != -1:
    idx_old = old_text.find('/yr"}', idx_old)
    print("OLD FILE:")
    print(old_text[idx_old-10:idx_old+150])
