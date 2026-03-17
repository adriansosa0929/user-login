if (loginBtn) {
    loginBtn.addEventListener('click', async () => {
      const id = authIdInput.value.trim();
      const pass = authPassInput.value.trim();
      if (id && pass) {
        try {
          const res = await fetch('http://localhost:5000/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id, password: pass })
          });
          const data = await res.json();
          if (data.success) {
            localStorage.setItem('kam_logged_in', 'true');
            localStorage.setItem('kam_current_user', id);
            localStorage.setItem('kam_tier', data.tier || 'Standard');
            updatePortalView();
          } else {
            authError.textContent = data.error || "Invalid credentials.";
            authError.style.display = 'block';
          }
        } catch (err) {
            authError.textContent = "Server connection failed.";
            authError.style.display = 'block';
        }
      } else {
        authError.textContent = "ID and Passcode cannot be empty.";
        authError.style.display = 'block';
      }
    });
  }
