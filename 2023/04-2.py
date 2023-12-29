# Advent of Code 2023
# Day 4: Scratchcards
# Part Two
# Written by Jeffrey Derksen

class Card:
    def __init__(self, winning_numbers: list, your_numbers: list) -> None:
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
        self.amount = 1

    def check_matches(self) -> int:
        matches = len(set(self.your_numbers).intersection(self.winning_numbers))
        return matches
    
    def copy_card(self) -> None:
        self.amount += 1


# Read in lines from input file
cards = []
with open('./2023/inputs/4.txt') as f:
    for line in f:
        numbers = line.strip().split(sep=':')[1].split(sep='|')
        cards.append(Card(numbers[0].split(), numbers[1].split()))

# Copy cards
total_cards = len(cards)
for i in range(len(cards)):
    matches = cards[i].check_matches()
    total_cards += matches * cards[i].amount
    for j in range(matches):
        for k in range(cards[i].amount):
            cards[i + j + 1].copy_card() 

print(total_cards)
