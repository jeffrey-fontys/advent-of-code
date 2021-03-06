# Advent of Code 2021
# Day 3: Binary Diagnostic
# Part Two
# Made by Jeffrey Derksen

with open('./2021/inputs/3.txt') as f:
    for line in f:
        bytes = f.readlines()


def calculate_rating(priority):
    stored_bytes = bytes[:]

    for i in range(12):
        count_ones = 0
        count_zeroes = 0
        for byte in stored_bytes:
            if byte[i] == "1":
                count_ones = count_ones + 1
            else:
                count_zeroes = count_zeroes + 1

        temp = []
        if count_ones < count_zeroes:
            for byte in stored_bytes:
                if byte[i] != priority:
                    temp.append(byte)
        else:
            for byte in stored_bytes:
                if byte[i] == priority:
                    temp.append(byte)
        stored_bytes = temp

        if len(stored_bytes) == 1:
            break

    return int(stored_bytes[0], 2)


oxygen_rating = calculate_rating("1")
co2_rating = calculate_rating("0")

print("Oxygen rating:", oxygen_rating)
print("CO2 rating:", co2_rating)
print("Multiplied:", oxygen_rating * co2_rating)
