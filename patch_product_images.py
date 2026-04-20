import re
import io

file_path = r'c:\Users\adria\Desktop\antigravity-website-1.0\index-uhv_Skau.js'

with io.open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we only replace inside the products array.
def replace_images(segment, new_image):
    return re.sub(r'image:"https://images\.unsplash\.com/[^"]+"', f'image:"{new_image}"', segment)

# Split by the categories to specifically target each one
m1 = re.search(r'gi=\{extremities:\{', text)
m2 = re.search(r'\},ocular:\{id:"ocular"', text)
m3 = re.search(r'\},cerebral:\{id:"cerebral"', text)
m4 = re.search(r'\}\}\};const ', text[m3.start():]) # find the end of cerebral

if m1 and m2 and m3 and m4:
    ext_start = m1.start()
    ext_end = m2.start()
    
    oc_start = m2.start()
    oc_end = m3.start()
    
    cer_start = m3.start()
    cer_end = m3.start() + m4.start()

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
    print("Could not find the splits correctly.")

