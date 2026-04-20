import os

target_file = '../index-uhv_Skau.js'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

form_start_str = ',s.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
form_start_idx = content.find(form_start_str)

button_end_str = 'children:"Submit Consultation Request"})})'
button_idx = content.find(button_end_str, form_start_idx)

if form_start_idx != -1 and button_idx != -1:
    slice_end_idx = button_idx + len(button_end_str)
    
    replacement = ',s.jsx("div", {className:"text-center p-8 bg-biometric-blue/5 border border-biometric-blue/20 rounded-xl mt-8 mx-auto max-w-2xl", children: s.jsxs("div", {children: [s.jsx("h3", {className:"text-2xl font-display text-biometric-blue mb-4", children:"Consultations Offline"}), s.jsx("p", {className:"text-gray-300 font-mono", children:"We have received an overwhelming number of requests and our consultation portal is temporarily suspended. Please refer to our company information below."})]})})'
    
    new_content = content[:form_start_idx] + replacement + content[slice_end_idx:]
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced the form inputs with an information block!")
else:
    print("COULD NOT FIND START OR END")
