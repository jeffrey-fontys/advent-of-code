# Advent of Code 2022
# Day 4: Camp Cleanup
# Part One
# Made by Jeffrey Derksen

pairs = []
with open('./2022/inputs/4.txt') as f:
    for line in f:
        line = line.strip()
        ranges = line.split(',')
        pairs.append(ranges)

fully_contained = 0
for pair in pairs:
    bounds_1 = pair[0].split('-')
    bounds_2 = pair[1].split('-')
    range_1 = [x for x in range(int(bounds_1[0]), int(bounds_1[1]) + 1)]
    range_2 = [x for x in range(int(bounds_2[0]), int(bounds_2[1]) + 1)]

    contains_1 = True
    for section in range_1:
        if section not in range_2: contains_1 = False
    
    contains_2 = True
    for section in range_2:
        if section not in range_1: contains_2 = False
    
    if contains_1 or contains_2: fully_contained += 1

print(fully_contained)
