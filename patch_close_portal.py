import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '''  // Close logic (if they want to hide it manually, though routing should handle most)
  closeBtn.addEventListener('click', () => {
    modalOverlay.classList.remove('active');
  });

  // Close on outside click
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      modalOverlay.classList.remove('active');
    }
  });'''

replacement = '''  // Close logic (if they want to hide it manually, though routing should handle most)
  function closeAndRoute() {
    modalOverlay.classList.remove('active');
    const path = window.location.pathname;
    if (path === '/orders' || path === '/account' || path === '/support') {
      window.location.href = '/';
    }
  }

  closeBtn.addEventListener('click', closeAndRoute);

  // Close on outside click
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) {
      closeAndRoute();
    }
  });'''

if target in text:
    text = text.replace(target, replacement)
    print("Replaced close routing!")
else:
    print("WARNING: close routing target not found")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

