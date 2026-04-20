import re
import io

file_path = r'c:\Users\adria\Documents\index.html'
try:
    with io.open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    idx = text.find('portal.js')
    if idx != -1:
        print(text[max(0, idx-100):min(len(text), idx+100)])
except FileNotFoundError:
    pass

file_path2 = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
try:
    with io.open(file_path2, 'r', encoding='utf-8') as f:
        text = f.read()

    idx = text.find('portal.js')
    if idx != -1:
        print(text[max(0, idx-100):min(len(text), idx+100)])
except FileNotFoundError:
    pass
