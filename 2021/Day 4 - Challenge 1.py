# Advent of Code 2021
# Day 4: Giant Squid
# Part One
# Made by Jeffrey Derksen

class Square:

    is_checked = False

    def __init__(self, number):
        self.number = number

class Board:

    def __init__(self, rows):
        self.rows = rows
    
    def check_square(self, number):
        for row in self.rows:
            for square in row:
                if square.number == number: square.is_checked = True
    
    def did_i_win(self):
        for row in self.rows:
            for square in row:
                if square.is_checked == False: break
            else: return True
        
        for i in range(5):
            for j in range(5):
                if self.rows[j][i].is_checked == False: break
            else: return True
        
        return False # Chula!

    def sum_unchecked(self):
        sum = 0
        for row in self.rows:
            for square in row:
                if square.is_checked == False: sum += square.number
        return sum

def draw_numbers():
    for number in numbers_drawn:
        for board in boards:
            board.check_square(number)
            if board.did_i_win():
                print(win_message, number * board.sum_unchecked())
                return

boards = []
with open('./2021/inputs/4.txt') as f:
    first_line = True
    row_count = 0
    rows = []
    for line in f:
        if first_line == True:
            numbers_drawn = [int(i) for i in line.split(sep=",")]
            first_line = False
        else:
            if line != "\n":
                
                if row_count == 5:
                    row_count = 0
                    boards.append(Board(rows))
                    rows = []

                board_row = []
                for i in range(5):
                    board_row.append(Square(int(line[i*3:i*3+2])))
                rows.append(board_row)
                row_count += 1

win_message = "Allamaraine! You've won the game! Your score is:"
draw_numbers()
