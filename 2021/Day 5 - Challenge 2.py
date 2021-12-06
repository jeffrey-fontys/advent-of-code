# Advent of Code 2021
# Day 5: Hydrothermal Venture
# Part Two
# Made by Jeffrey Derksen

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
    
    def is_x_line(self):
        if self.y1 == self.y2: return True
        else: return False

    def is_y_line(self):
        if self.x1 == self.x2: return True
        else: return False

    def is_diagonal(self):
        if abs(self.y1 - self.y2) == abs(self.x1 - self.x2): return True
        else: return False
    
    def has_length(self):
        if self.x1 == self.x2: return abs(self.y1 - self.y2) + 1
        elif self.y1 == self.y2: return abs(self.x1 - self.x2) + 1
        else: return abs(self.x1 - self.x2) + 1

lines = []
with open('./2021/inputs/5.txt') as f:
    for line in f:
        coords = line.split(sep=" -> ")
        coords_1 = coords[0].split(sep=",")
        coords_2 = coords[1].split(sep=",")
        lines.append(Line(coords_1[0], coords_1[1], coords_2[0], coords_2[1]))

chart = [[0 for x in range(1000)] for y in range(1000)]
count = 0
for line in lines:
    if line.is_x_line():
        for i in range(line.has_length()):
            if line.x1 < line.x2: chart[line.y1][line.x1 + i] += 1
            else: chart[line.y1][line.x1 - i] += 1
    elif line.is_y_line():
        for i in range(line.has_length()):
            if line.y1 < line.y2: chart[line.y1 + i][line.x1] += 1
            else: chart[line.y1 - i][line.x1] += 1
    elif line.is_diagonal():
        for i in range(line.has_length()):
            if line.x1 < line.x2 and line.y1 > line.y2:
                chart[line.y1 - i][line.x1 + i] += 1
            elif line.x1 > line.x2 and line.y1 < line.y2:
                chart[line.y1 + i][line.x1 - i] += 1
            elif line.x1 < line.x2 and line.y1 < line.y2:
                chart[line.y1 + i][line.x1 + i] += 1
            else: chart[line.y1 - i][line.x1 - i] += 1

count = 0
for row in chart:
    for point in row:
        if point > 1: count += 1

print(f"There are {count} points where at least two lines overlap.")
