import sys

target_file = '../index-uhv_Skau.js'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_str = 's.jsxs(U.form,'
idx = content.find(start_str)
if idx == -1:
    # Try singular jsx
    start_str = 's.jsx(U.form,'
    idx = content.find(start_str)

if idx == -1:
    print("Could not find U.form!")
    sys.exit(1)

# Start matching from the letter 's'
# Function signature is s.jsxs(...)
match_idx = content.find('(', idx)
if match_idx == -1:
    print("Could not find opening paren!")
    sys.exit(1)

depth = 0
end_idx = -1
for i in range(match_idx, len(content)):
    if content[i] == '(':
        depth += 1
    elif content[i] == ')':
        depth -= 1
        if depth == 0:
            end_idx = i
            break

if end_idx == -1:
    print("Could not match parentheses!")
    sys.exit(1)

# slice out from idx to end_idx + 1
replacement = 's.jsx("div", {className:"text-center p-8 bg-biometric-blue/5 border border-biometric-blue/20 rounded-xl", children: s.jsx("h3", {className:"text-xl text-biometric-blue font-bold", children:"Consultations are currently offline."})})'

new_content = content[:idx] + replacement + content[end_idx+1:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Patched successfully! Replaced {end_idx+1 - idx} characters.")
