import subprocess
import os

print("Running Product Images 2:")
print(subprocess.run(['python', 'patch_product_images2.py'], capture_output=True, text=True).stdout)

print("Running Other Images:")
print(subprocess.run(['python', 'patch_other_images.py'], capture_output=True, text=True).stdout)

print("Running Product Images 1:")
print(subprocess.run(['python', 'patch_product_images.py'], capture_output=True, text=True).stdout)

print("Bumping Cache:")
try:
    with open('../index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('v=11', 'v=12')
    with open('../index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Bumped to v12")
except Exception as e:
    print(e)
