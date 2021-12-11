# Advent of Code 2021
# Day 11: Dumbo Octopus
# Part One
# Made by Jeffrey Derksen

class Octopus:
    has_flashed = False
    energy = 0

    def __init__(self, energy):
        self.energy = energy

    def flash(self, matrix, x, y):
        if self.energy <= 9 or self.has_flashed:
            return

        self.has_flashed = True
        NEIGHBOURS = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x + 1, y],
                      [x + 1, y + 1], [x, y + 1], [x - 1, y + 1], [x - 1, y]]
        for neighbour in NEIGHBOURS:
            x, y = neighbour
            if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
                matrix[y][x].energy += 1
                matrix[y][x].flash(matrix, x, y)


matrix = []
with open('./2021/inputs/11.txt') as f:
    for line in f:
        input = line.strip()
        row = [Octopus(int(item)) for item in input]
        matrix.append(row)

step = 1
while True:
    local_flashes = 0

    for row in matrix:
        for octopus in row:
            octopus.energy += 1

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x].flash(matrix, x, y)

    for row in matrix:
        for octopus in row:
            if octopus.has_flashed:
                local_flashes += 1
                octopus.energy = 0
                octopus.has_flashed = False

    if local_flashes == 100:
        print(f'First step during which all octopuses flash: {step}')
        break

    step += 1
