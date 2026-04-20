import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index.html'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inject a global error catcher that writes to a div on the screen
error_catcher = '''
<script>
window.onerror = function(msg, url, line, col, error) {
    document.body.innerHTML = "<div style='color:red; font-size:24px; padding: 20px;'>SYNTAX ERROR: " + msg + "<br>Line: " + line + ":" + col + "</div>";
    return false;
};
</script>
'''

if 'window.onerror' not in text:
    text = text.replace('<body>', '<body>\n' + error_catcher)
    
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected error catcher into index.html")
else:
    print("Error catcher already exists.")
