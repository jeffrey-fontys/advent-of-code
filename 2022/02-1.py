# Advent of Code 2022
# Day 2: Rock Paper Scissors
# Part One
# Made by Jeffrey Derksen

# 1 = Rock, 2 = Paper, 3 = Scissors
letter_to_move = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

class Round:
    def __init__(self, move1: str, move2: str) -> None:
        self.move_opponent = letter_to_move[move1]
        self.move_player = letter_to_move[move2]
        self.calculate_score()
    
    def calculate_score(self) -> None:
        if self.move_player == self.move_opponent:
            self.score = 3
        elif self.move_player == 1 and self.move_opponent == 3 or \
            self.move_player == 2 and self.move_opponent == 1 or \
            self.move_player == 3 and self.move_opponent == 2:
            self.score = 6
        else:
            self.score = 0
        
        self.score += self.move_player


def calculate_total_score(round_list: list) -> int:
    total = 0

    for round in round_list:
        total += round.score
    
    return total


rounds = []
with open('./2022/inputs/2.txt') as f:
    for line in f:
        moves = line.split()
        rounds.append(Round(moves[0], moves[1]))

print(calculate_total_score(rounds))
