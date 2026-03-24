with open('input4.txt', 'r', encoding = 'utf-8') as file_in:
    for line in file_in:
        if len(line.rstrip()) > 20:
            with open('output4.txt', 'a', encoding = 'utf-8') as file_out:
                file_out.write(line)
