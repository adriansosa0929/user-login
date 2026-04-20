import os

target_file = '../index-uhv_Skau.js'
with open(target_file, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'onClick:()=>x("consultation"),className:"w-full mt-8 bg-white/5 hover:bg-biometric-blue hover:text-black border border-white/20 hover:border-transparent text-white font-bold py-3 rounded-lg transition-all text-sm uppercase tracking-widest",children:"Request Consultation"'

print('Count:', text.count(target))

if text.count(target) == 1:
    print("Found exact match. Generating replacement.")
