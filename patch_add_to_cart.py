import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Main product page
text = re.sub(r'children:"Add to Cart"\}\),n&&s\.jsx\(V,\{to:`/customize/\$\{i\.id\}`',
              r'children:`Add to Cart - $${i.price.toLocaleString()}`}),n&&s.jsx(V,{to:`/customize/${i.id}`', text)

# 2. Installation Services ($5,000)
text = text.replace('price:5000,image:"/categories/bionic.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart"})',
                    'price:5000,image:"/categories/bionic.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $5,000"})')

# 3. Neural Interfacing Sync ($800)
text = text.replace('price:800,image:"/categories/cerebral.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart"})',
                    'price:800,image:"/categories/cerebral.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $800"})')

# 4. Maintenance & Repair ($500)
text = text.replace('price:500,image:"/categories/ocular.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart"})',
                    'price:500,image:"/categories/ocular.png"}),className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Add to Cart - $500"})')

# 5. Standard Care ($500)
text = text.replace('price:500,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart"})',
                    'price:500,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-white/10 hover:bg-biometric-blue hover:text-black font-bold text-xs uppercase tracking-widest rounded transition-all text-white",children:"Add to Cart - $500"})')

# 6. Gold Tier ($1,200)
text = text.replace('price:1200,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-biometric-blue text-black font-bold text-xs uppercase tracking-widest rounded hover:bg-white transition-all",children:"Add to Cart"})',
                    'price:1200,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-biometric-blue text-black font-bold text-xs uppercase tracking-widest rounded hover:bg-white transition-all",children:"Add to Cart - $1,200"})')

# 7. Platinum Elite ($2,500)
text = text.replace('price:2500,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart"})',
                    'price:2500,image:"/categories/bionic.png"}),className:"px-4 py-2 bg-purple-500 hover:bg-purple-400 text-white font-bold text-xs uppercase tracking-widest rounded transition-all",children:"Add to Cart - $2,500"})')


with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Add to Cart patches applied.")
