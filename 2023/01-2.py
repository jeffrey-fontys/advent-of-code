# Advent of Code 2023
# Day 1: Trebuchet?!
# Part Two
# Written by Jeffrey Derksen

digits_spelled = {
    'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9'
}

def check_line(line: str) -> list:
    set = []
    for i in range(len(line)):
        if line[i].isnumeric():
            set.append(line[i])
        else:
            for digit_spelled, digit in digits_spelled.items():
                if line[i : i + len(digit_spelled)] == digit_spelled:
                    set.append(digit)
    return set

# Read in lines from input file
input_lines = []
with open('./2023/inputs/1.txt') as f:
    for line in f:
        input_lines.append(line)

# Extract integers from each line
digit_lines = []
for line in input_lines:
    digit_lines.append(check_line(line))

# Count up total
total = 0
for line in digit_lines:
    total += int(line[0] + line[-1])

print(total)
