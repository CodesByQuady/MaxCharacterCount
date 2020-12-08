def max_char_count(Text):
    max_char = ''
    max_count = 0
    for char in set(Text):
        count = Text.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

print(max_char_count('Cookie')) #This should print o
print(max_char_count('Banana')) #This should print a
print(max_char_count('Smoothie')) #This should print o

