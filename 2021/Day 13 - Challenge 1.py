# Advent of Code 2021
# Day 13: Transparent Origami
# Part One
# Made by Jeffrey Derksen

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

coordinates = fold(instructions[0][0], int(instructions[0][2:]))

print(len(coordinates))
