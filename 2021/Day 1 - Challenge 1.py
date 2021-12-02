# Day 1 - Challenge 1
# Made by Jeffrey Derksen
# 2021-12-01

numbers = []
with open('./inputs/1.txt') as f:
    for line in f:
        numbers.append(int(line))

count = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        count = count + 1

print(count)