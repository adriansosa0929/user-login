import subprocess
import os

os.chdir('..')
# Restore from git
print(subprocess.run(['git', 'checkout', 'index-uhv_Skau.js'], capture_output=True, text=True).stdout)

# Run patches
os.chdir('user-login')
print("Running Add to Cart:")
print(subprocess.run(['python', 'patch_add_to_cart.py'], capture_output=True, text=True).stdout)

print("Running About Us Float:")
print(subprocess.run(['python', 'patch_about_us_float.py'], capture_output=True, text=True).stdout)

print("Running Order Conf Robust:")
print(subprocess.run(['python', 'patch_order_conf_robust.py'], capture_output=True, text=True).stdout)

print("Running Hide Elements:")
print(subprocess.run(['python', 'hide_elements_safe.py'], capture_output=True, text=True).stdout)

print("Bumping Cache:")
print(subprocess.run(['python', 'bust_cache6.py'], capture_output=True, text=True).stdout)
# We can bump cache with bust_cache6.py which increments to v=10, wait let's just make v=11!
