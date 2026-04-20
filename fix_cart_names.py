import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# I want to add `name:"...",` right after `title:"...",` so that `name` exists and the shopping cart doesn't break
# I will find all instances of `title:"(something)",price:` and replace with `title:"\1",name:"\1",price:` using a python regex
new_text = re.sub(r'title:("[^"]+"),price:', r'title:\1,name:\1,price:', text)

if new_text != text:
    print("Found and replaced title elements with name elements.")
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
else:
    print("No replacements were made. Let's check regex manually.")

