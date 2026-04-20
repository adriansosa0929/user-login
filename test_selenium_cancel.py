import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

try:
    print("Navigating to index...")
    driver.get("http://127.0.0.1:5000/")
    
    # inject kam_orders
    driver.execute_script("""
        localStorage.setItem('kam_logged_in', 'true');
        localStorage.setItem('kam_current_user', 'Admins');
        localStorage.setItem('kam_orders', JSON.stringify([
            {name: 'Titan Arm V2', price: 5000, added_at: new Date().getTime()}
        ]));
    """)
    print("Injected kam_orders.")
    
    # Open orders directly
    driver.get("http://127.0.0.1:5000/orders")
    time.sleep(1)
    
    # Check if there is an item
    cards = driver.find_elements('css selector', '.kam-order-card')
    print(f"Found {len(cards)} cards.")
    
    # Click cancel
    cancel_btns = driver.find_elements('css selector', '.kam-btn-return')
    if cancel_btns:
        print("Clicking cancel button...")
        
        # Override window.confirm so it auto-accepts
        driver.execute_script("window.confirm = function() { return true; }")
        
        cancel_btns[0].click()
        time.sleep(1)
        
        cards_after = driver.find_elements('css selector', '.kam-order-card')
        print(f"Found {len(cards_after)} cards after cancel.")
        
        # Get console logs
        logs = driver.get_log('browser')
        for l in logs:
            print(l)
    else:
        print("No cancel button found.")
finally:
    driver.quit()
