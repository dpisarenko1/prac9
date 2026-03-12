# write a function to convert a date in the form of dd.mm to a day number
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_day_number(date_str):
    day, month = map(int, date_str.split('.'))
    return sum(days_in_month[:month -1 ]) + day

result = []
with open('input10.txt', 'r', encoding = 'utf-8') as file_in:
    current_date = get_day_number(file_in.readline().strip())
    count = int(file_in.readline())
    for number_of_line in range(count):
        id_of_cell, storage_start = file_in.readline().strip().split()
        storage_start_day = get_day_number(storage_start)

        if current_date - storage_start_day > 3:
            result.append(id_of_cell)

with open('output10.txt', 'w', encoding = 'utf-8') as file_out:
    file_out.write("\n".join(result))