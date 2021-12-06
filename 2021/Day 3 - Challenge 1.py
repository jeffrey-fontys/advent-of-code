# Advent of Code 2021
# Day 3: Binary Diagnostic
# Part One
# Made by Jeffrey Derksen

with open('./2021/inputs/3.txt') as f:
    for line in f:
        bytes = f.readlines()

gamma = ""
for i in range(12):
    count_ones = 0
    count_zeroes = 0
    for byte in bytes:
        if byte[i] == "1": count_ones = count_ones + 1
        else: count_zeroes = count_zeroes + 1
    
    if count_ones > count_zeroes: gamma = gamma + "1"
    else: gamma = gamma + "0"

epsilon = ""
for char in gamma:
    if char == "1": epsilon = epsilon + "0"
    else: char = epsilon = epsilon + "1"

print("Gamma rate:", int(gamma, 2))
print("Epsilon rate:", int(epsilon, 2))
print("Multiplied", int(gamma, 2) * int(epsilon, 2))
