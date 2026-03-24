with open('input1.txt', 'r', encoding = 'utf-8') as file:
    result = ''.join([x.upper() for x in file])

    with open('output1.txt', 'w', encoding = 'utf-8') as file_out:
        file_out.write(result)
