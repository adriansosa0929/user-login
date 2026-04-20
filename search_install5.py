import re
with open(r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js', encoding='utf-8') as f:
    text = f.read()

# Let's search for the "Add to Cart" buttons in index-uhv_Skau.js
matches = re.finditer(r'Add to Cart', text)
output = []
for m in matches:
    output.append(text[max(0, m.start() - 200) : min(len(text), m.end() + 200)])

if not output:
    print("No 'Add to Cart' found in the entire file.")
else:
    for i, o in enumerate(output):
        print(f"Match {i}:")
        print(o)
        print("-----")
