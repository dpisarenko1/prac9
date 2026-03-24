result = None
try:
    with open('input6.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()

    count = int(lines[0].strip())
    real_lines_count = len(lines) - 1

    result = 'YES' if real_lines_count == count else 'NO'

except ValueError:
    result = 'ERROR'

with open('output6.txt', 'w', encoding = 'utf-8') as file_out:
    file_out.write(result)
