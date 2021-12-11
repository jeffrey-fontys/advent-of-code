# Advent of Code 2021
# Day 9: Smoke Basin
# Part Two
# Made by Jeffrey Derksen

map = []
with open('./2021/inputs/9.txt') as f:
    for line in f:
        line_stripped = line.strip()
        numbers_in_row = [int(number) for number in line_stripped]
        map.append(numbers_in_row)

last_row = len(map) - 1
last_col = len(map[0]) - 1
low_points = []

for y in range(last_row + 1):
    for x in range(last_col + 1):
        number = map[y][x]
        low_point = True
        if y != 0 and number >= map[y - 1][x]:
            low_point = False
        if x != last_col and number >= map[y][x + 1]:
            low_point = False
        if y != last_row and number >= map[y + 1][x]:
            low_point = False
        if x != 0 and number >= map[y][x - 1]:
            low_point = False
        if low_point:
            low_points.append([y, x])


# Flood fill algorithm, see https://en.wikipedia.org/wiki/Flood_fill.
def flood_fill(y, x):
    # If point exceeds boundaries of map, return.
    if y < 0 or y >= last_row + 1 or x < 0 or x >= last_col + 1:
        return 0

    # If point is a 9 (upper limit) or 10 (already part of basin), return.
    if map[y][x] == 9 or map[y][x] == 10:
        return 0

    map[y][x] = 10
    count = 1
    count += flood_fill(y + 1, x)  # Recurse and look below.
    count += flood_fill(y - 1, x)  # Recurse and look above.
    count += flood_fill(y, x + 1)  # Recurse and look right.
    count += flood_fill(y, x - 1)  # Recurse and look left.
    return count


basins = []
for low_point in low_points:
    y = low_point[0]
    x = low_point[1]
    basin_size = flood_fill(y, x)
    basins.append(basin_size)

basins.sort(reverse=True)
largest_basins_multiplied = basins[0] * basins[1] * basins[2]

print('The sizes of the three largest basins multiplied '
      f'is {largest_basins_multiplied}.')
