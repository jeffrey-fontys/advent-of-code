# Advent of Code 2023
# Day 4: Scratchcards
# Part One
# Written by Jeffrey Derksen

class Card:
    def __init__(self, winning_numbers: list, your_numbers: list) -> None:
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers

    def calculate_value(self) -> int:
        value = 0
        for number in self.your_numbers:
            if number in self.winning_numbers:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        return value


# Read in lines from input file
cards = []
with open('./2023/inputs/4.txt') as f:
    for line in f:
        numbers = line.strip().split(sep=':')[1].split(sep='|')
        cards.append(Card(numbers[0].split(), numbers[1].split()))

# Calculate sum of card values
sum = 0
for card in cards:
    sum += card.calculate_value()

print(sum)
