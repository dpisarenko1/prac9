with open('input3.txt', 'r', encoding = 'utf-8') as f:
    word = ''

    for line in f:
        word = word + (str(line[0]))

with open('output3.txt', 'w', encoding = 'utf-8') as file_out:
    file_out.write(word)
