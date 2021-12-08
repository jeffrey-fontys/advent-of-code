# Advent of Code 2021
# Day 8: Seven Segment Search
# Part One
# Made by Jeffrey Derksen

output_values = []
with open('./2021/inputs/8.txt') as f:
    for line in f:
        line_split = line.split(sep="|")
        second_split = [item for item in line_split[1].strip().split(sep=" ")]
        output_values.append(second_split)

count = [0 for _ in range(4)]
for line in output_values:
    for value in line:
        if len(value) == 2: count[0] += 1 # Number 1
        elif len(value) == 4: count[1] += 1 # Number 4
        elif len(value) == 3: count[2] += 1 # Number 7
        elif len(value) == 7: count[3] += 1 # Number 8

print(f"The digits 1, 4, 7 and 8 appear {sum(count)} times in the output values.")
