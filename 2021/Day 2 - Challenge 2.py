# Advent of Code 2021
# Day 2: Dive!
# Part Two
# Made by Jeffrey Derksen

x = 0
y = 0
aim = 0

values = []
with open('./2021/inputs/2.txt') as f:
    for line in f:
        values.append(line.split(sep=" "))

for set in values:
    if set[0] == "forward":
        x = x + int(set[1])
        y = y + aim * int(set[1])
    if set[0] == "down":
        aim = aim + int(set[1])
    if set[0] == "up":
        aim = aim - int(set[1])

print("Horizontal position:", x)
print("Depth:", y)
print("Multiplied:", x * y)
