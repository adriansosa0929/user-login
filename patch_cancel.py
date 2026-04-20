import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the renderOrders function to allow actionLabel for 'Processing'
target1 = '''          if (order._status === 'Processing') {
            statusHtml = '<span class="kam-status-badge status-processing" style="background: rgba(234, 179, 8, 0.2); color: #eab308; align-self: flex-start;">Processing</span>';
            // No action label - cannot cancel until checked out!
          } else if (order._status === 'Processing Delivery') {'''

replacement1 = '''          if (order._status === 'Processing') {
            statusHtml = '<span class="kam-status-badge status-processing" style="background: rgba(234, 179, 8, 0.2); color: #eab308; align-self: flex-start;">Processing</span>';
            actionLabel = 'Remove Item';
          } else if (order._status === 'Processing Delivery') {'''

if target1 in text:
    text = text.replace(target1, replacement1)
    print("Replaced target1 (added actionLabel for Processing)")
else:
    print("WARNING: target1 not found.")

# 2. Update the click listener for the return button to handle 'cart' source
target2 = '''          if (source === 'kam_orders') {
            let history = [];
            try { history = JSON.parse(localStorage.getItem('kam_orders') || '[]'); } catch (err) { }
            const index = history.findIndex(i => (i.name || i.title || 'KAM System Prototype Variation') === productName);
            if (index !== -1) {
              // Radically erase the item from order history
              history.splice(index, 1);
              localStorage.setItem('kam_orders', JSON.stringify(history));
              renderOrders();
            }
          }'''

replacement2 = '''          if (source === 'kam_orders') {
            let history = [];
            try { history = JSON.parse(localStorage.getItem('kam_orders') || '[]'); } catch (err) { }
            const index = history.findIndex(i => (i.name || i.title || 'KAM System Prototype Variation') === productName);
            if (index !== -1) {
              history.splice(index, 1);
              localStorage.setItem('kam_orders', JSON.stringify(history));
              renderOrders();
            }
          } else if (source === 'cart') {
            let currentCart = [];
            try { currentCart = JSON.parse(localStorage.getItem('cart') || '[]'); } catch (err) { }
            const index = currentCart.findIndex(i => (i.name || i.title || 'KAM System Prototype Variation') === productName);
            if (index !== -1) {
              currentCart.splice(index, 1);
              localStorage.setItem('cart', JSON.stringify(currentCart));
              renderOrders();
            }
          }'''

if target2 in text:
    text = text.replace(target2, replacement2)
    print("Replaced target2 (added cart removal logic)")
else:
    print("WARNING: target2 not found.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

