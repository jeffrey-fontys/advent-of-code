# Advent of Code 2022
# Day 1: Calorie Counting
# Part Two
# Made by Jeffrey Derksen

class Elf:
    calories = 0

    def add_calories(self, amount):
        self.calories += amount

elves = [Elf()]
with open('./2022/inputs/1.txt') as f:
    for line in f:
        if line == '\n':
            elves.append(Elf())
        else:
            elves[-1].add_calories(int(line))

elves.sort(key=lambda elf: elf.calories, reverse=True)

print(elves[0].calories + elves[1].calories + elves[2].calories)
