file = open('input4.txt','r',encoding = 'utf-8')

for line in file:
    if len(line.rstrip()) > 20:
        open('output4.txt', 'a', encoding = 'utf-8').write(line)