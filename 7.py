with open('input7.txt', 'r', encoding = 'utf-8') as file_in:
    lines = file_in.readlines()

lines_to_write = []

for line in lines:
    if line.strip() != '100':
        lines_to_write.append(line)

with open('input7.txt', 'w', encoding = 'utf-8') as file_out:
    file_out.writelines(lines_to_write)
