# Advent of Code 2022
# Day 3: Rucksack Reorganization
# Part One
# Made by Jeffrey Derksen

backpacks = []
with open('./2022/inputs/3.txt') as f:
    for line in f:
        line = line.strip()
        compartment_1 = line[:len(line)//2]
        compartment_2 = line[len(line)//2:]
        backpacks.append([compartment_1, compartment_2])

sum = 0
for backpack in backpacks:
    shared_item = ''
    for char in backpack[0]:
        if char in backpack[1]: shared_item = char
    
    if shared_item.isupper(): sum += ord(shared_item) - 38
    else: sum += ord(shared_item) - 96

print(sum)
