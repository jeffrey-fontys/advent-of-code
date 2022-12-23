# Advent of Code 2022
# Day 2: Rock Paper Scissors
# Part One
# Made by Jeffrey Derksen

# X = lose(0), Y = draw(3), Z = win(6)
# A = rock(1), B = paper(2), C = scissors(3)
scores = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2
    },
    'Y': {
        'A': 4,
        'B': 5,
        'C': 6
    },
    'Z': {
        'A': 8,
        'B': 9,
        'C': 7
    }
}

score = 0
with open('./2022/inputs/2.txt') as f:
    for line in f:
        moves = line.split()
        score += scores[moves[1]][moves[0]]

print(score)
