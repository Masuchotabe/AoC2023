import re

number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()
list_number = []
for line in input_data.split('\n'):
    number = 0
    regex = r'(?=(\d|' + "|".join(number_dict.keys()) + "))"
    digits = re.findall(regex, line)
    if len(digits) > 1:
        first_one = number_dict.get(digits[0], digits[0])
        number = int(str(number_dict.get(digits[0], digits[0])) + str(number_dict.get(digits[-1], digits[-1])))
    elif len(digits) == 1:
        number = int(str(number_dict.get(digits[0], digits[0])) * 2)
    list_number.append(number)

print(sum(list_number))
