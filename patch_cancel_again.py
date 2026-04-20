import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '''          let deleted = false;
          if (source === 'kam_orders') {
            let history = [];
            try { history = JSON.parse(localStorage.getItem('kam_orders') || '[]'); } catch (err) { }
            const index = history.findIndex(i => {
                const p = i.name || i.title || 'KAM System Prototype Variation';
                return p.trim() === productName;
            });
            if (index !== -1) {
              history.splice(index, 1);
              localStorage.setItem('kam_orders', JSON.stringify(history));
              deleted = true;
            } else {
               alert("Could not find exactly matching item in system log.");
            }
          } else if (source === 'cart') {
            let currentCart = [];
            try { currentCart = JSON.parse(localStorage.getItem('cart') || '[]'); } catch (err) { }
            const index = currentCart.findIndex(i => {
                const p = i.name || i.title || 'KAM System Prototype Variation';
                return p.trim() === productName;
            });
            if (index !== -1) {
              currentCart.splice(index, 1);
              localStorage.setItem('cart', JSON.stringify(currentCart));
              deleted = true;
            } else {
               alert("Could not find matching cart item.");
            }
          }

          if (deleted) {
              renderOrders();
              // Dispatch events to try indicating to the React application that the cache mutated
              window.dispatchEvent(new Event('storage'));
              
              // Additionally, force a dispatch so React definitely updates
              const ev = new CustomEvent('kam_cart_removed', { detail: { name: productName } });
              window.dispatchEvent(ev);
          }'''

replacement = '''          let deleted = false;
          if (source === 'kam_orders') {
            let history = [];
            try { history = JSON.parse(localStorage.getItem('kam_orders') || '[]'); } catch (err) { }
            const index = history.findIndex(i => {
                const p = i.name || i.title || 'KAM System Prototype Variation';
                return p.trim() === productName.trim() || productName.includes(p.trim());
            });
            if (index !== -1) {
              history.splice(index, 1);
              localStorage.setItem('kam_orders', JSON.stringify(history));
              deleted = true;
            } else {
               alert("Could not find exactly matching item in system log: " + productName);
            }
          } else if (source === 'cart') {
            let currentCart = [];
            try { currentCart = JSON.parse(localStorage.getItem('cart') || '[]'); } catch (err) { }
            const index = currentCart.findIndex(i => {
                const p = i.name || i.title || 'KAM System Prototype Variation';
                return p.trim() === productName.trim() || productName.includes(p.trim());
            });
            if (index !== -1) {
              currentCart.splice(index, 1);
              localStorage.setItem('cart', JSON.stringify(currentCart));
              deleted = true;
            } else {
               alert("Could not find matching cart item: " + productName);
            }
          }

          if (deleted) {
              renderOrders();
              setTimeout(() => alert("Order successfully cancelled and removed from history!"), 200);
              // Dispatch events to try indicating to the React application that the cache mutated
              window.dispatchEvent(new Event('storage'));
              
              // Additionally, force a dispatch so React definitely updates
              const ev = new CustomEvent('kam_cart_removed', { detail: { name: productName } });
              window.dispatchEvent(ev);
              
              // Radical sync back to React just in case it's a cart item
              if (source === 'cart') {
                 try {
                   setTimeout(() => {
                     localStorage.setItem('cart', localStorage.getItem('cart'));
                     window.dispatchEvent(new Event('storage'));
                   }, 100);
                 } catch(e) {}
              }
          }'''

if target in text:
    text = text.replace(target, replacement)
    print("Patched listener for extreme safety with visual feedback.")
else:
    print("WARNING: target not found.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

