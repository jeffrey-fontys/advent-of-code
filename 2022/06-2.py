# Advent of Code 2022
# Day 6: Tuning Trouble
# Part Two
# Made by Jeffrey Derksen

datastream = ''
with open('./2022/inputs/6.txt') as f:
    for line in f:
        datastream = line

chars_processed = 0
marker_found = False
window_size = 14
while not marker_found:
    chars_processed += 1

    if chars_processed < window_size: continue

    slice = datastream[chars_processed-window_size:chars_processed]
    set_list = set(slice)

    if len(set_list) == window_size: marker_found = True

print(chars_processed)
