with open('input8.txt', 'r', encoding = 'utf-8') as file:
    steps = [int(line.strip()) for line in file.readlines()]

days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(steps) == '366':
    days_in_each_month[1] = 29

current_index = 0
averages_per_month = []

for days in days_in_each_month:
    average = sum(steps[current_index:current_index + days]) / days
    averages_per_month.append(average)
    current_index += days

with open('output8.txt', 'w', encoding = 'utf-8') as file_out:
    for average in averages_per_month:
        file_out.write(str(average) + '\n')

