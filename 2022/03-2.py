# Advent of Code 2022
# Day 3: Rucksack Reorganization
# Part Two
# Made by Jeffrey Derksen

backpacks = [[]]
with open('./2022/inputs/3.txt') as f:
    for line in f:
        line = line.strip()
        if len(backpacks[-1]) == 3: backpacks.append([])
        backpacks[-1].append(line)

sum = 0
for group in backpacks:
    shared_item = ''
    for i in range(3):
        for char in group[i]:
            if char in group[0] and char in group[1] and char in group[2]: 
                shared_item = char

    if shared_item.isupper(): sum += ord(shared_item) - 38
    else: sum += ord(shared_item) - 96

print(sum)
