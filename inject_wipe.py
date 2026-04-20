import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

wipe_logic = '''
// --- ONE TIME WIPE PER USER REQUEST ---
if (localStorage.getItem('kam_cleared_history_v1') !== 'true') {
    localStorage.setItem('kam_orders', '[]');
    localStorage.setItem('cart', '[]');
    localStorage.setItem('kam_cleared_history_v1', 'true');
}
// ------------------------------------

'''

# Inject at the top right after window.kam_is_returning...
if '// Start interval to sync' in text:
    text = text.replace('// Start interval to sync', wipe_logic + '// Start interval to sync')
else:
    # Just prepend
    text = wipe_logic + text

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected local storage wipe.")
