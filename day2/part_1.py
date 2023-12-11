import re

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()

index_sum = 0
for line in input_data.split('\n'):
    print(line)
    index = int(line.split(":")[0][5:])
    red_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} red", line.split(":")[1])]
    green_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} green", line.split(":")[1])]
    blue_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} blue", line.split(":")[1])]
    if max(red_numbers) <= 12 and max(green_numbers) <= 13 and max(blue_numbers) <= 14:
        index_sum += index

print(index_sum)
