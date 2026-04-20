import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We found secure@kam.bio earlier. Did they want employee1@kamindustries.local to visually replace secure@kam.bio?
if 'secure@kam.bio' in text:
    print("Found secure@kam.bio visually displayed!")
    text = text.replace('secure@kam.bio', 'employee1@kamindustries.local')
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced visual email to employee1@kamindustries.local")

