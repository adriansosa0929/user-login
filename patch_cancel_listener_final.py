import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '''  // Handle return/cancel order logic
  document.addEventListener('click', (e) => {
    if (e.target && e.target.classList.contains('kam-btn-return')) {
      const orderCard = e.target.closest('.kam-order-card');
      if (orderCard) {
        const source = orderCard.getAttribute('data-source');
        if (confirm('Are you sure you want to cancel or refund this order?')) {
          window.kam_is_returning = true;
          const productName = orderCard.getAttribute('data-name') || orderCard.querySelector('h3').textContent;

          if (source === 'kam_orders') {
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
          }

          // Dispatch events to try indicating to the React application that the cache mutated
          window.dispatchEvent(new Event('storage'));
          setTimeout(() => { window.kam_is_returning = false; }, 500);
        }
      }
    } else if (e.target && e.target.classList.contains('kam-btn-track')) {'''


replacement = '''  // Handle return/cancel order logic
  document.addEventListener('click', (e) => {
    const returnBtn = e.target.closest('.kam-btn-return');
    if (returnBtn) {
      const orderCard = returnBtn.closest('.kam-order-card');
      if (orderCard) {
        const source = orderCard.getAttribute('data-source');
        if (confirm('Are you sure you want to cancel or remove this item?')) {
          window.kam_is_returning = true;
          
          let productName = orderCard.getAttribute('data-name');
          if (!productName) {
            const h3 = orderCard.querySelector('h3');
            if (h3) productName = h3.textContent.trim();
          }

          let deleted = false;
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
          }
          
          setTimeout(() => { window.kam_is_returning = false; }, 500);
        }
      }
    } else if (e.target && e.target.classList.contains('kam-btn-track')) {'''

if target in text:
    text = text.replace(target, replacement)
    print("Success replacing complex listener!")
else:
    print("WARNING: Could not perfectly match listener.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

