# Advent of Code 2021
# Day 10: Syntax Scoring
# Part One
# Made by Jeffrey Derksen

ALLOWED_PAIRS = {'(':')', '[':']', '{':'}', '<':'>'}
SCORES = {')':3, ']':57, '}':1197, '>':25137}
        
def scan_line(line):
    for i in range(len(line)):
        if line[i] not in [')',']','}','>']:
            result = block_check(line, i + 1, line[i])
            if result != 0: return result
    return 0

def block_check(line, start, block_open):
    opens_passed = 0
    for i in range(start, len(line)):
        if line[i] not in [')',']','}','>']:
            opens_passed += 1
        elif opens_passed == 0 and line[i] == ALLOWED_PAIRS[block_open]:
            return 0
        elif opens_passed == 0: return SCORES[line[i]]
        else: opens_passed -= 1
    return 0

score = 0
with open('./2021/inputs/10.txt') as f:
    for line in f:
        score += scan_line(line)

print(f'The total syntax error score is {score}.')
