import re

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()

power_sum = 0
for line in input_data.split('\n'):
    print(line)
    index = int(line.split(":")[0][5:])
    red_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} red", line.split(":")[1])]
    green_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} green", line.split(":")[1])]
    blue_numbers = [int(s.split(" ")[0]) for s in re.findall(r"\d{1,2} blue", line.split(":")[1])]
    power_sum += max(red_numbers) * max(green_numbers) * max(blue_numbers)

print(power_sum)
