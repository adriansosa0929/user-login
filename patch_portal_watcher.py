import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Auto-open orders to bypass auth for Guest when checkout occurs
target_watcher = '''        localStorage.setItem('kam_orders', JSON.stringify(history));

        // If the portal is currently open, refresh the view instantly
        if (typeof renderOrders === 'function') renderOrders();
      }'''

replacement_watcher = '''        localStorage.setItem('kam_orders', JSON.stringify(history));

        // Let's create an anonymous account and open the portal
        if (localStorage.getItem('kam_logged_in') !== 'true') {
          localStorage.setItem('kam_logged_in', 'true');
          localStorage.setItem('kam_current_user', 'Guest');
        }
        if (typeof openKamPortal === 'function') openKamPortal('orders');
        
        // If the portal is currently open, refresh the view instantly
        if (typeof renderOrders === 'function') renderOrders();
      }'''

if target_watcher in text:
    text = text.replace(target_watcher, replacement_watcher)
    print("Patched watcher.")
else:
    print("Watcher not found.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

