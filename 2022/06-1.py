# Advent of Code 2022
# Day 6: Tuning Trouble
# Part One
# Made by Jeffrey Derksen

datastream = ''
with open('./2022/inputs/6.txt') as f:
    for line in f:
        datastream = line

chars_processed = 3
marker_found = False
while not marker_found:
    slice = datastream[chars_processed-3:chars_processed+1]
    set_list = set(slice)

    if len(set_list) == 4: marker_found = True

    chars_processed += 1

print(chars_processed)
