# Advent of Code 2021
# Day 14: Extended Polymerization
# Part One
# Made by Jeffrey Derksen

from collections import Counter

insertion_rules = {}
with open('./2021/inputs/14.txt') as f:
    section = 0
    for line in f:
        if line == '\n':
            section += 1
        elif section == 0:
            template = line.strip()
        else:
            split = line.strip().split(sep=' -> ')
            insertion_rules.update({split[0]: split[1]})

for _ in range(10):
    new_template = ''
    for i in range(len(template)):
        window = template[i:i + 2]
        new_template += template[i]
        for rule in insertion_rules:
            if window == rule:
                new_template += insertion_rules[rule]
                break
    template = new_template

template_counted = Counter(template).most_common()
print('Result is:', template_counted[0][1] - template_counted[-1][1])
