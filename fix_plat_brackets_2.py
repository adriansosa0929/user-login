import io

file_path = '../index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

bad = 'children:"Add to Cart - $2,500"})]})]})]})]})]})},Yi=({title:e'
good = 'children:"Add to Cart - $2,500"})]})]})]})]})]})]})},Yi=({title:e'

if bad in text:
    text = text.replace(bad, good)
    print("Added one more ]})")
else:
    print("Could not find the target string!")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

