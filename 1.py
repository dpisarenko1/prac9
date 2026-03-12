file = open('input1.txt','r', encoding = 'utf-8')
result = ''.join([x.upper() for x in file])
open('output1.txt','w', encoding = 'utf-8').write(result)