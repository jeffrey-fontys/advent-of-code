# Advent of Code 2021
# Day 7: The Treachery of Whales
# Part Two
# Made by Jeffrey Derksen

with open('./2021/inputs/7.txt') as f:
    line_read = f.read().split(sep=",")
    crab_positions = [int(item) for item in line_read]

position_range = max(crab_positions) + 1
fuel_used = [0 for _ in range(position_range)]
for i in range(position_range):
    for position in crab_positions:
        distance = abs(position - i)
        fuel_used[i] += (distance * (distance + 1)) // 2

print(f"The least amount of fuel the crabs must spend is {min(fuel_used)}.")
