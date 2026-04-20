import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function renderTickets()')
if idx != -1:
    print(text[idx:idx+1500])

idx2 = text.find('kam-btn-ticket')
if idx2 != -1:
    print("\n--- Listener for create ticket ---")
    print(text[idx2-200:idx2+800])
