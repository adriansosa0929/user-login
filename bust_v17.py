import io

html_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('index-uhv_Skau.js?v=16', 'index-uhv_Skau.js?v=17')

with io.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
