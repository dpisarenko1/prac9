import os

with open('input9.txt', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()

os.makedirs('simple', exist_ok=True)

number = 1
out_lines = []

for line in lines:
    if number % 2 == 0:
        out_lines.append(line)
    else:
        pass
    number += 1

with open('simple/output9.txt', 'w', encoding = 'utf-8') as file_out:
    file_out.writelines(line for line in out_lines)
