# Advent of Code 2021
# Day 1: Sonar Sweep
# Part One
# Made by Jeffrey Derksen

numbers = []
with open('./2021/inputs/1.txt') as f:
    for line in f:
        numbers.append(int(line))

count = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        count = count + 1

print(count)
