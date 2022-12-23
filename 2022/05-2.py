# Advent of Code 2022
# Day 5: Supply Stacks
# Part Two
# Made by Jeffrey Derksen

matrix = []
stack_amount = 0
instructions = []
with open('./2022/inputs/5.txt') as f:
    for line in f:
        if '[' in line:
            matrix.append(line.strip('\n'))
        elif line[0] == ' ' and stack_amount == 0:
            stack_amount = int(line.strip().split()[-1])
        elif line[0] == 'm':
            line_split = line.strip().split()
            instructions.append([
                int(line_split[1]),
                int(line_split[3]) - 1,
                int(line_split[5]) - 1
            ])

stacks = []
for i in range(stack_amount):
    stack = []
    for j in range(len(matrix) - 1, -1, -1):
        crate = matrix[j][i * 4 + 1]
        if crate != ' ': stack.append(crate)
    stacks.append(stack)

for instruction in instructions:
    crates = []
    for i in range(instruction[0]):
        crate = stacks[instruction[1]].pop(-1)
        crates.append(crate)

    crates.reverse()
    stacks[instruction[2]].extend(crates)

top_crates = ''.join([x[-1] for x in stacks])

print(top_crates)
