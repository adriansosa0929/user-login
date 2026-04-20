import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\server.py'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

header_logic = '''
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    # This ensures browsers absolutely always fetch fresh files during dev
    return r
'''

if 'def add_header' not in text:
    if "app = Flask(__name__" in text:
        text = text.replace("app = Flask(__name__, static_folder='.')", "app = Flask(__name__, static_folder='.')\napp.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0\n" + header_logic)
        

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Patched server.py to disable cache.")
