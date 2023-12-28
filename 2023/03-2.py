# Advent of Code 2023
# Day 3: Gear Ratios
# Part Two
# Written by Jeffrey Derksen

class Gear:
    def __init__(self, valid_positions: list) -> None:
        self.valid_positions = valid_positions
        self.numbers = []
        self.ratio = 0

    def add_number(self, number: int) -> None:
        self.numbers.append(number)

    def calculate_ratio(self) -> None:
        if len(self.numbers) != 2:
            return
        self.ratio = self.numbers[0] * self.numbers[1]


def check_gears(gears: list[Gear], positions: list) -> None:
    for gear in gears:
        for position in positions:
            if position in gear.valid_positions:
                gear.add_number(int(number))
                break


# Read in lines from input file
input_lines = []
with open('./2023/inputs/3.txt') as f:
    for line in f:
        input_lines.append(line.strip())

# Find valid positions
gears = []
for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        char = input_lines[y][x]
        if char == '*':
            check = []
            check.extend([
                [x - 1, y],
                [x - 1, y - 1],
                [x, y - 1],
                [x + 1, y - 1],
                [x + 1, y],
                [x + 1, y + 1],
                [x, y + 1],
                [x - 1, y + 1]
            ])
            valid_positions = []
            for position in check:
                if input_lines[position[1]][position[0]].isnumeric():
                    valid_positions.append(position)
            gears.append(Gear(valid_positions))

# Find valid numbers
for y in range(len(input_lines)):
    positions = []
    number = ''
    for x in range(len(input_lines[y])):
        char = input_lines[y][x]
        if char.isnumeric():
            positions.append([x, y])
            number += char
        else:
            check_gears(gears, positions)
            positions = []
            number = ''
    if number != '':
        check_gears(gears, positions)

sum = 0
for gear in gears:
    gear.calculate_ratio()
    sum += gear.ratio

print(sum)
