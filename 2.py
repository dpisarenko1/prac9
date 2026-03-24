with open('input2.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        if line[0].lower() == 'a':
            with open('output2.txt', 'a', encoding = 'utf-8') as file_out:
                file_out.write(line)
