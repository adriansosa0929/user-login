import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\portal.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '''  // Handle Form Submission
  ticketForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const sub = document.getElementById('ticketSubject').value;
    const cat = document.getElementById('ticketCategory').value;
    const bod = document.getElementById('ticketBody').value;

    const newTicket = {
      id: Date.now().toString(),
      subject: sub,
      category: cat,
      body: bod,
      status: 'Open',
      timestamp: Date.now()
    };

    tickets.push(newTicket);
    localStorage.setItem('kam_tickets', JSON.stringify(tickets));

    // Reset and re-render
    ticketForm.reset();
    renderTickets();
  });'''

replacement = '''  // Handle Form Submission
  ticketForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const sub = document.getElementById('ticketSubject').value;
    const cat = document.getElementById('ticketCategory').value;
    const bod = document.getElementById('ticketBody').value;

    // Launch default email client
    const emailBody = `Category: ${cat}%0D%0A%0D%0AIssue Description:%0D%0A${encodeURIComponent(bod)}`;
    window.location.href = `mailto:support@kamindustries.demo?subject=${encodeURIComponent(sub)}&body=${emailBody}`;

    const newTicket = {
      id: Date.now().toString(),
      subject: sub,
      category: cat,
      body: bod,
      status: 'Open',
      timestamp: Date.now()
    };

    tickets.push(newTicket);
    localStorage.setItem('kam_tickets', JSON.stringify(tickets));

    // Reset and re-render
    ticketForm.reset();
    renderTickets();
  });'''


if target in text:
    text = text.replace(target, replacement)
    print("Ticket listener patched.")
else:
    # Try finding kamFormTicket if ticketForm not found
    print("WARNING: Target not found.")

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

