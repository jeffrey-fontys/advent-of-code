# Advent of Code 2021
# Day 13: Transparent Origami
# Part Two
# Made by Jeffrey Derksen

def print_matrix() -> None:
    for row in matrix:
        for field in row:
            print(field, end='')
        print()


def fold(fold_axis: str, fold_location: int) -> None:
    if fold_axis == 'x':
        index = 0
    else:
        index = 1
    
    for coordinate in coordinates:
        if coordinate[index] > fold_location:
            coordinate[index] -= 2 * (coordinate[index] - fold_location)

    res = []
    [res.append(x) for x in coordinates if x not in res]
    return res


coordinates = []
instructions = []
with open('./2021/inputs/13.txt') as f:
    section = 0
    for line in f:
        if line == '\n':
            section += 1
        elif section == 0:
            split = line.strip().split(sep=',')
            coordinates.append([int(split[0]), int(split[1])])
        else:
            instructions.append(line.strip()[11:])

for instruction in instructions:
    coordinates = fold(instruction[0], int(instruction[2:]))

max_x = max([value[0] for value in coordinates])
max_y = max([value[1] for value in coordinates])

matrix = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for coordinate in coordinates:
    matrix[coordinate[1]][coordinate[0]] = '#'

print_matrix()
