import re

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()
list_number = []
for line in input_data.split('\n'):
    number = 0
    digits = re.findall(r'\d', line)
    if len(digits) > 1:
        first_one = number_dict
        number = int(str(digits[0]) + str(digits[-1]))
    elif len(digits) == 1:
        number = int(str(digits[0]) * 2)
    list_number.append(number)

print(sum(list_number))
