# Advent of Code 2021
# Day 14: Extended Polymerization
# Part One
# Made by Jeffrey Derksen

from collections import Counter

insertion_rules = {}
pairs_template = {}
elements = {}
with open('./2021/inputs/14.txt') as f:
    section = 0
    for line in f:
        if line == '\n':
            section += 1
        elif section == 0:
            template = line.strip()
        else:
            split = line.strip().split(sep=' -> ')
            insertion_rules.update({split[0]: split[0][0] + split[1]})
            pairs_template.update({split[0]: 0})
            elements.update({split[1]: 0})

for element in template:
    elements[element] += 1

pairs = pairs_template.copy()
for i in range(len(template) - 1):
    window = template[i:i + 2]
    pairs.update({window: pairs[window] + 1})

for _ in range(40):
    pass_pairs = pairs_template.copy()
    for pair in pairs:
        pair_count = pairs[pair]
        if pair_count != 0:
            new_pair_1 = insertion_rules[pair]
            new_pair_2 = insertion_rules[pair][1] + pair[1]
            pass_pairs.update({new_pair_1: pair_count +
                               pass_pairs[new_pair_1]})
            pass_pairs.update({new_pair_2: pair_count +
                               pass_pairs[new_pair_2]})
            elements[insertion_rules[pair][1]] += pair_count
    pairs = pass_pairs

elements_counted = Counter(elements).most_common()
print('Result is:', elements_counted[0][1] - elements_counted[-1][1])
