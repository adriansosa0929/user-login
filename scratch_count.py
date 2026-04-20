text = open('../index-uhv_Skau.js', 'r', encoding='utf-8').read()
target = 'className:"grid grid-cols-1 md:grid-cols-2 gap-6"'
print('Count:', text.count(target))
