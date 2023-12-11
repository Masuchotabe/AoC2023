import re

with open('input_data/data.txt', 'r') as file:
    input_data = file.read()

total_sum = 0
cards = input_data.split('\n')
scratchcard_copies = {}
for index, card in enumerate(cards):
    card_name = card.split(":")[0]
    numbers = card.split(":")[1]
    winning_numbers = re.findall(r"\d+", numbers.split("|")[0])
    game_numbers = re.findall(r"\d+", numbers.split("|")[1])
    first = True
    game_score = 0
    for n in winning_numbers:
        if n in game_numbers:
            if first:
                game_score = 1
                first = False
            else:
                game_score *= 2
    if game_score:
        # print(range(index, index + game_score))
        print(range(index, min(index + game_score, len(cards))))
        for x in range(index, min(index + game_score, len(cards))):
            temp_card_name = cards[x].split(":")[0]
            if temp_card_name in scratchcard_copies:
                scratchcard_copies[temp_card_name] += scratchcard_copies.get(card_name, 1)
            else:
                scratchcard_copies[temp_card_name] = scratchcard_copies.get(card_name, 1)
    total_sum += game_score
# print(f"{total_sum=}")
print(scratchcard_copies)
