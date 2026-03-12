file = open('input2.txt','r',encoding = 'utf-8')

for line in file:
    if line[0].lower() == 'a':
        file = open('output2.txt','a',encoding = 'utf-8').write(line)