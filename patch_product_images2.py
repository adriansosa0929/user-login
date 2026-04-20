import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

def replace_images(segment, new_image):
    return re.sub(r'image:"https://images\.unsplash\.com/[^"]+"', f'image:"{new_image}"', segment)

m1 = re.search(r'gi=\{extremities:\{', text)
m2 = re.search(r'\]\},ocular:\{id:"ocular"', text)
m3 = re.search(r'\]\},cerebral:\{id:"cerebral"', text)

if m1 and m2 and m3:
    ext_start = m1.start()
    ext_end = m2.start()
    
    oc_start = m2.start()
    oc_end = m3.start()
    
    cer_start = m3.start()
    
    # Try to find the end of cerebral array
    # It ends with ]} then something else. Let's just find `]}\}` or similar, or just replace for the next 4000 characters.
    m4 = re.search(r'\]\}\}\};', text[cer_start:])
    if not m4:
        # fallback
        m4 = re.search(r'\]\}\}', text[cer_start:])
        
    cer_end = cer_start + m4.start() if m4 else cer_start + 4000

    extremities_part = text[ext_start:ext_end]
    ocular_part = text[oc_start:oc_end]
    cerebral_part = text[cer_start:cer_end]
    
    new_ext = replace_images(extremities_part, "./kam_bionic_arm.png")
    new_oc = replace_images(ocular_part, "./kam_ocular_implant.png")
    new_cer = replace_images(cerebral_part, "./kam_cerebral_chip.png")
    
    new_text = text[:ext_start] + new_ext + new_oc + new_cer + text[cer_end:]
    
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    print("Replaced product images successfully.")
else:
    print("m1:", bool(m1), "m2:", bool(m2), "m3:", bool(m3))

