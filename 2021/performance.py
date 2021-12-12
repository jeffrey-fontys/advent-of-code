import os
import runpy
from time import perf_counter

file_count = len(os.listdir('2021')) // 2 - 1
times = [perf_counter()]
for i in range(file_count):
    runpy.run_path(f'2021/Day {i + 1} - Challenge 1.py')
    times.append(perf_counter())
    runpy.run_path(f'2021/Day {i + 1} - Challenge 2.py')
    times.append(perf_counter())

for i in range(file_count):
    part1_time = round((times[i*2+1]-times[i*2]) * 1000, 2)
    part2_time = round((times[i*2+2]-times[i*2+1]) * 1000, 2)
    print('Day', format(i + 1, "<2"), end=" | ")
    print("Part 1 ->", f"{part1_time}ms".rjust(9), end=" | ")
    print("Part 2 ->", f"{part2_time}ms".rjust(9))

print(f"Total time: {round(times[-1]-times[0], 4)}s")
