import glob

for f in sorted(glob.glob('patch_*.py')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        if 'index-uhv_Skau.js' in content:
            print(f)
