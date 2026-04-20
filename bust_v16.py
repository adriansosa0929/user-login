import io

html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=13', 'index-uhv_Skau.js?v=16')
html = html.replace('index-uhv_Skau.js?v=14', 'index-uhv_Skau.js?v=16')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped to v16")
