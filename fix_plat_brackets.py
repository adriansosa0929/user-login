import io
import re

file_path = '../index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We know check_syntax fails at 185719.
# The corrupted string is somewhere there.
# Let's fix the brackets. 
old_bad = 'children:"Add to Cart - $2,500"})]}))]})]})]})]})]})},Yi='
new_good = 'children:"Add to Cart - $2,500"})]})]})]})]})]})},Yi='

if old_bad in text:
    text = text.replace(old_bad, new_good)
    print("Fixed Platinum Elite brackets!")
else:
    print("Could not find the exact bad string. Finding with regex...")
    match = re.search(r'children:"Add to Cart - \$2,500"\})\]\}\)\)\]\}\)\]\}\)\]\}\)\]\}\)\]\}\),Yi=', text)
    if match:
        text = text[:match.start()] + new_good + text[match.end():]
        print("Fixed Platinum Elite brackets with regex!")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

