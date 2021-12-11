# Advent of Code 2021
# Day 8: Seven Segment Search
# Part Two
# Made by Jeffrey Derksen

def compare(number_to_compare_with, shared, digit_list):
    for digit in digit_list:
        count = 0
        for char in digit:
            if char in number_to_compare_with:
                count += 1
        if count == shared:
            return digit


signal_values = []
output_values = []
with open('./2021/inputs/8.txt') as f:
    for line in f:
        line_split = line.split(sep="|")

        second_split_signal = [
            item for item in line_split[0].strip().split(sep=" ")]
        signal_values.append(second_split_signal)

        second_split_output = [
            item for item in line_split[1].strip().split(sep=" ")]
        output_values.append(second_split_output)

count = 0
output_i = 0
for line in signal_values:
    output_value = ""
    number_values = [0 for x in range(10)]
    five_segments = []
    six_segments = []
    for value in line:
        if len(value) == 2:
            number_values[1] = value
        elif len(value) == 4:
            number_values[4] = value
        elif len(value) == 3:
            number_values[7] = value
        elif len(value) == 7:
            number_values[8] = value
        elif len(value) == 5:
            five_segments.append(value)
        else:
            six_segments.append(value)

    number_values[2] = compare(number_values[4], 2, five_segments)
    five_segments.remove(number_values[2])
    number_values[3] = compare(number_values[7], 3, five_segments)
    five_segments.remove(number_values[3])
    number_values[5] = five_segments[0]

    number_values[6] = compare(number_values[7], 2, six_segments)
    six_segments.remove(number_values[6])
    number_values[9] = compare(number_values[4], 4, six_segments)
    six_segments.remove(number_values[9])
    number_values[0] = six_segments[0]

    for value in output_values[output_i]:
        for i in range(10):
            if len(value) != len(number_values[i]):
                continue
            for char in value:
                if char not in number_values[i]:
                    break
            else:
                output_value += str(i)
    count += int(output_value)
    output_i += 1


print(f"You get {count} if you add up all the output values.")
