with open('input5.txt', 'r', encoding = 'utf-8') as file_in:
    numbers = []
    try:
        for line in file_in:
            numbers.append(int(line.rstrip()))
        result = numbers[0] / numbers[1] + numbers[2]
        open('output5.txt', 'a', encoding = 'utf-8').write(str(result))

    except ValueError:
        with open('output5.txt', 'a', encoding = 'utf-8') as file_out:
            file_out.write('data error')

    except ZeroDivisionError:
        with open('output5.txt', 'a', encoding = 'utf-8') as file_out:
            file_out.write('division by 0')
