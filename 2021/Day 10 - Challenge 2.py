# Advent of Code 2021
# Day 10: Syntax Scoring
# Part Two
# Made by Jeffrey Derksen

import statistics

ALLOWED_PAIRS = {'(':')', '[':']', '{':'}', '<':'>'}
SCORE_VALUES = {')':1, ']':2, '}':3, '>':4}
scores = []
        
def scan_line(line):
    end_blocks = []
    score = 0
    for i in range(len(line)):
        if line[i] not in [')',']','}','>']:
            result = block_check(line, i + 1, line[i])
            if result == 1: return 0
            elif result == 2: end_blocks.append(ALLOWED_PAIRS[line[i]])
    end_blocks.reverse()
    for end_block in end_blocks:
        score = score * 5 + SCORE_VALUES[end_block]
    return score

def block_check(line, start, block_open):
    opens_passed = 0
    for i in range(start, len(line)):
        if line[i] not in [')',']','}','>']:
            opens_passed += 1
        elif opens_passed == 0 and line[i] == ALLOWED_PAIRS[block_open]:
            return 0
        elif opens_passed == 0: return 1
        else: opens_passed -= 1
    return 2

with open('./2021/inputs/10.txt') as f:
    for line in f:
        result = scan_line(line.strip())
        if result > 0: scores.append(result)

MEDIAN = statistics.median(scores)

print(f'The middle score is {MEDIAN}.')
