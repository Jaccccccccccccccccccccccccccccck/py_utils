the_string="abc"
for char in the_string[:]:
    char_count = {}
    char_count_most = {'most_count': None, 'most_count_chars':[]}
    if char in char_count.keys():
        char_count[char] += 1
    else:
        char_count[char] = 1
    if char_count[char]:
        pass
