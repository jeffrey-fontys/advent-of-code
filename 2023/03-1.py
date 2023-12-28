# Advent of Code 2023
# Day 3: Gear Ratios
# Part One
# Written by Jeffrey Derksen

# Read in lines from input file
input_lines = []
with open('./2023/inputs/3.txt') as f:
    for line in f:
        input_lines.append(line.strip())

# Find valid positions
valid_positions = []
for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        char = input_lines[y][x]
        if char != '.' and not char.isnumeric():
            valid_positions.extend([
                [x - 1, y],
                [x - 1, y - 1],
                [x, y - 1],
                [x + 1, y - 1],
                [x + 1, y],
                [x + 1, y + 1],
                [x, y + 1],
                [x - 1, y + 1]
            ])

# Find valid numbers
valid_numbers = []
for y in range(len(input_lines)):
    positions = []
    number = ''
    for x in range(len(input_lines[y])):
        char = input_lines[y][x]
        if char.isnumeric():
            positions.append([x, y])
            number += char
        else:
            for position in positions:
                if position in valid_positions:
                    valid_numbers.append(int(number))
                    break
            positions = []
            number = ''
    if number != '':
        for position in positions:
            if position in valid_positions:
                valid_numbers.append(int(number))
                break

print(sum(valid_numbers))
