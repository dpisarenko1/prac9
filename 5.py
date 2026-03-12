file = open('input5.txt', 'r', encoding = 'utf-8')
numbers = []

try:
    for line in file:
        numbers.append(int(line.rstrip()))
    result = numbers[0] / numbers[1] + numbers[2]
    open('output5.txt', 'a', encoding = 'utf-8').write(str(result))

except ValueError:
    open('output5.txt', 'a', encoding = 'utf-8').write('data error')

except ZeroDivisionError:
    open('output5.txt', 'a', encoding = 'utf-8').write('division by 0')
