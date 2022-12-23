# Advent of Code 2022
# Day 1: Calorie Counting
# Part One
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

most_calories = 0
for elf in elves:
    if elf.calories > most_calories:
        most_calories = elf.calories

print(most_calories)
