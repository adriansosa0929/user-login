import io
import re

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'
with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r's\.jsx\(V,\{to:"/request",className:"w-full block text-center bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Request Consultation"\}\)', text)
print("Count for V-style Requests:", len(matches))

matches_px6 = re.findall(r's\.jsx\(V,\{to:"/request",className:"px-6 py-2 bg-biometric-blue text-black font-bold rounded uppercase tracking-widest text-sm hover:bg-white transition-all",children:"Request Consultation"\}\)', text)
print("Count for px6-style Requests:", len(matches_px6))
