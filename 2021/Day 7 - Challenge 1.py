# Advent of Code 2021
# Day 7: The Treachery of Whales
# Part One
# Made by Jeffrey Derksen

with open('./2021/inputs/7.txt') as f:
    line_read = f.read().split(sep=",")
    crab_positions = [int(item) for item in line_read]

max_position = max(crab_positions)
fuel_used = [0 for _ in range(max_position + 1)]
for i in range(max_position + 1):
    for position in crab_positions:
        fuel_used[i] += abs(position - i)

print(f"The least amount of fuel the crabs must spend is {min(fuel_used)}.")
