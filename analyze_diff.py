import io

with io.open(r'c:\Users\adria\Desktop\antigravity-website-1.0\user-login\diff.txt', 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

# Let's count how many + and - lines exist in diff.txt to see the scope
plus_lines = [line for line in text.split('\n') if line.startswith('+') and not line.startswith('+++')]
minus_lines = [line for line in text.split('\n') if line.startswith('-') and not line.startswith('---')]

print(f"Total + lines: {len(plus_lines)}")
print(f"Total - lines: {len(minus_lines)}")

# Give a snippet of unique lines added (the progress that was wiped)
print("\nUnique additions wiped out:")
for line in plus_lines[:20]:
    print(line[:150])
