# Advent of Code 2021
# Day 6: Lanternfish
# Part One
# Made by Jeffrey Derksen

class Lanternfish:

    def __init__(self, age):
        self.age = age

    def will_spawn(self) -> bool:
        if self.age == 0:
            self.age = 6
            return True
        else:
            self.age -= 1
            return False


with open('./2021/inputs/6.txt') as f:
    for line in f:
        ages_split = line.split(sep=",")
        initial_ages = [int(item) for item in ages_split]

lanternfish_list = [Lanternfish(age) for age in initial_ages]

days = 80
for i in range(days):
    new_fish = 0
    for lanternfish in lanternfish_list:
        if lanternfish.will_spawn():
            new_fish += 1
    for j in range(new_fish):
        lanternfish_list.append(Lanternfish(8))

print(f"After {days} days there will be {len(lanternfish_list)} lanternfish.")
