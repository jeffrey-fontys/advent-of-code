# Advent of Code 2022
# Day 4: Camp Cleanup
# Part Two
# Made by Jeffrey Derksen

pairs = []
with open('./2022/inputs/4.txt') as f:
    for line in f:
        line = line.strip()
        ranges = line.split(',')
        pairs.append(ranges)

overlapping_ranges = 0
for pair in pairs:
    bounds_1 = pair[0].split('-')
    bounds_2 = pair[1].split('-')
    range_1 = [x for x in range(int(bounds_1[0]), int(bounds_1[1]) + 1)]
    range_2 = [x for x in range(int(bounds_2[0]), int(bounds_2[1]) + 1)]

    overlap = False
    for section in range_1:
        if section in range_2: overlap = True
    
    contains_2 = True
    for section in range_2:
        if section in range_1: overlap = True
    
    if overlap: overlapping_ranges += 1

print(overlapping_ranges)
