# Advent of Code 2021
# Day 1: Sonar Sweep
# Part Two
# Made by Jeffrey Derksen

numbers = []
with open('./2021/inputs/1.txt') as f:
    for line in f:
        numbers.append(int(line))

windows = []
for i in range(len(numbers) - 2):
    windows.append(numbers[i] + numbers[i+1] + numbers[i+2])

count = 0
for i in range(len(windows) - 1):
    if windows[i] < windows[i + 1]:
        count = count + 1

print(count)
