import io
import re

file_path = r'../index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Target Standard Cart string block that needs to be deduped
# We look for the first button's closing brace `]})` followed directly by `s.jsx("button", ... Add to Cart - $500"})`
std_dup_pattern = r'children:"Add to Cart - \$500"\}\)\]\}\),s\.jsx\("button",\{onClick:\(\)=>\{.*?,children:"Add to Cart - \$500"\}\)'
text = re.sub(std_dup_pattern, 'children:"Add to Cart - $500"})]}', text)

plat_dup_pattern = r'children:"Add to Cart - \$2,500"\}\)\]\}\),s\.jsx\("button",\{onClick:\(\)=>\{.*?,children:"Add to Cart - \$2,500"\}\)'
text = re.sub(plat_dup_pattern, 'children:"Add to Cart - $2,500"})]}', text)

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Duplicates removed.")
