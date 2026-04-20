import io

with io.open(r'c:\Users\adria\Desktop\antigravity-website-1.0\user-login\diff.txt', 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

# Print the last 1000 characters of the diff
print(text[-2000:])
