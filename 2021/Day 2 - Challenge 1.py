# Day 2 - Challenge 1
# Made by Jeffrey Derksen
# 2021-12-01

x = 0
y = 0

values = []
with open('./inputs/2.txt') as f:
    for line in f:
        values.append(line.split(sep=" "))

for set in values:
    if set[0] == "forward":
        x = x + int(set[1])
    if set[0] == "down":
        y = y + int(set[1])
    if set[0] == "up":
        y = y - int(set[1])

print("Horizontal position:", x)
print("Depth:", y)
print("Multiplied:", x * y)