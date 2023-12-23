# Advent of Code 2023
# Day 1: Trebuchet?!
# Part One
# Written by Jeffrey Derksen

lines = []
with open('./2023/inputs/1.txt') as f:
    for line in f:
        numbers = []
        for char in line:
            if char.isnumeric(): numbers.append(char)
        lines.append(numbers)

total = 0
for line in lines:
    total += int(line[0] + line[-1])

print(total)
