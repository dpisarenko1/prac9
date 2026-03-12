file = open('input3.txt', 'r', encoding = 'utf-8')
word = ''

for line in file:
    word = word + (str(line[0]))

open('output3.txt', 'w', encoding = 'utf-8').write(word)