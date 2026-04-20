import io

with io.open('old_index.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('bg-purple-500 hover:bg-purple-400')
if idx != -1:
    end_idx = text.find('Yi=', idx)
    print("TARGET IN OLD:")
    print(text[idx-50:end_idx+3])
