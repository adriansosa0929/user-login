import codecs

with codecs.open('../index-uhv_Skau.js', 'r', 'utf-8') as f:
    text = f.read()

def check_braces(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for i, c in enumerate(s):
        if c in '({[':
            stack.append((c, i))
        elif c in ')}]':
            if not stack:
                return f"Unmatched closing '{c}' at {i}:\n" + s[max(0, i-40):i+40]
            top_c, top_i = stack.pop()
            if pairs[c] != top_c:
                return f"Mismatched '{c}' at {i}, expected closing for '{top_c}' from {top_i}:\n" + s[max(0, i-40):i+40]
    
    if stack:
        top_c, top_i = stack.pop()
        return f"Unmatched opening '{top_c}' at {top_i}:\n" + s[max(0, top_i-40):top_i+40]
    
    return "OK, all brackets match!"

# This very naive checker will fail on strings and regexes! So let's do a slightly better one that ignores strings.

def check_braces_smart(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    i = 0
    in_str = False
    str_char = ''
    while i < len(s):
        c = s[i]
        
        # handle strings
        if not in_str and c in '"\'`':
            in_str = True
            str_char = c
            i += 1
            continue
            
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == str_char:
                in_str = False
            i += 1
            continue

        if c in '({[':
            stack.append((c, i))
        elif c in ')}]':
            if not stack:
                return f"Unmatched closing '{c}' at {i}:\n" + s[max(0, i-50):i+50]
            top_c, top_i = stack.pop()
            if pairs[c] != top_c:
                return f"Mismatched '{c}' at {i}, expected closing for '{top_c}' from {top_i}:\n" + s[max(0, i-50):i+50]
        i += 1
        
    if stack:
        top_c, top_i = stack.pop()
        return f"Unmatched opening '{top_c}' at {top_i}:\n" + s[max(0, top_i-40):top_i+40]
    return "OK"

print(check_braces_smart(text))
