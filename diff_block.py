import io
old_text = io.open('old_index.js', 'r', encoding='utf-8').read()
new_text = io.open('../index-uhv_Skau.js', 'r', encoding='utf-8').read()

start_str = 's.jsxs(U.div,{initial:{opacity:0,x:20}'

idx_old = old_text.find(start_str)
end_old = old_text.find(',Yi=', idx_old)

idx_new = new_text.find(start_str)
end_new = new_text.find(',Yi=', idx_new)

print("--- OLD BLOCK END ---")
print(old_text[end_old-150:end_old])
print("--- NEW BLOCK END ---")
print(new_text[end_new-150:end_new])
