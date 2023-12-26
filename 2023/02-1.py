# Advent of Code 2023
# Day 2: Cube Conundrum
# Part One
# Written by Jeffrey Derksen

class Game:
    def __init__(self, id: int, line: str) -> None:
        self.id = id
        self.line = line
        self.max_red = 0
        self.max_green = 0
        self.max_blue = 0
        self.determine_max()

    def determine_max(self) -> None:
        sets = self.line.split(sep=':')
        sets = sets[1].strip().split(sep=';')
        game_sets = []

        for set in sets:
            cubes = set.split(sep=',')
            for cube in cubes:
                cubes_split = cube.split()
                game_sets.append(cubes_split)

        for game_set in game_sets:
            if game_set[1] == 'red':
                self.max_red = max(self.max_red, int(game_set[0]))
            elif game_set[1] == 'green':
                self.max_green = max(self.max_green, int(game_set[0]))
            elif game_set[1] == 'blue':
                self.max_blue = max(self.max_blue, int(game_set[0]))

    def is_possible(self, red: int, green: int, blue: int) -> bool:
        if red < self.max_red or green < self.max_green or blue < self.max_blue:
            return False
        else:
            return True


# Read in lines from input file
games = []
with open('./2023/inputs/2.txt') as f:
    id_count = 0
    for line in f:
        id_count += 1
        games.append(Game(id_count, line))

# Determine how many games are possible
sum = 0
for game in games:
    if game.is_possible(12, 13, 14):
        sum += game.id

print(sum)
