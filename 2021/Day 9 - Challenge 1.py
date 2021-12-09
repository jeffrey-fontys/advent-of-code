# Advent of Code 2021
# Day 9: Smoke Basin
# Part One
# Made by Jeffrey Derksen

map = []
with open('./2021/inputs/9.txt') as f:
    for line in f:
        line_stripped = line.strip()
        numbers_in_row = [int(number) for number in line_stripped]
        map.append(numbers_in_row)

last_row = len(map) - 1
last_col = len(map[0]) - 1
sum_risk_level = 0

for y in range(last_row + 1):
    for x in range(last_col + 1):
        number = map[y][x]
        low_point = True
        if y != 0 and number >= map[y - 1][x]: low_point = False
        if x != last_col and number >= map[y][x + 1]: low_point = False
        if y != last_row and number >= map[y + 1][x]: low_point = False
        if x != 0 and number >= map[y][x - 1]: low_point = False
        if low_point: sum_risk_level += number + 1

print(f'The sum of risk levels is {sum_risk_level}.')
