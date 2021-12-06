# Advent of Code 2021
# Day 6: Lanternfish
# Part Two
# Made by Jeffrey Derksen

import numpy as np

with open('./2021/inputs/6.txt') as f:
    input_array = np.fromstring(f.read(), sep=",", dtype=int)

fish_bins = np.bincount(input_array, minlength=9)
days = 256
for _ in range(days):
    fish_bins = np.roll(fish_bins, -1)
    fish_bins[6] += fish_bins[8]

print(f"After {days} days there will be {np.sum(fish_bins)} lanternfish.")
