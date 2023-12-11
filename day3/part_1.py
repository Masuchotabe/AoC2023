import re

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()

total_sum = 0
line_tab = input_data.split('\n')


def is_around_symbol(tab, line_index, number):
    if line_index == 0:
        y_range = [line_index, line_index + 1]
    elif line_index == len(tab) - 1:
        y_range = [line_index - 1, line_index]
    else:
        y_range = [line_index - 1, line_index, line_index + 1]
        # for n in range(line_index - 1, line_index + 1):
    x_range = [max(number.start(0) - 1, 0), min(number.end(0) + 1, len(tab[0]))]
    # print(tab[y_range[0]:y_range[-1] + 1])
    for line in tab[y_range[0]:y_range[-1] + 1]:
        # print(line[x_range[0]:x_range[-1]])
        for c in line[x_range[0]:x_range[-1]]:

            if c not in '0123456789.':
                print(c)
                return True
    return False


for index, line in enumerate(line_tab):
    print(line)
    for m in re.finditer(r"\d+", line):
        print(m[0], is_around_symbol(line_tab, index, m))
        if is_around_symbol(line_tab, index, m):
            # print(m.string)
            total_sum += int(m[0])

print(f"{total_sum=}")
