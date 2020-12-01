#!/usr/bin/env python

import copy

with open('input.txt', 'r', encoding='utf-8') as input:
    lines = []
    for line in input:
        lines.append(line.rstrip())

    lines = list(map(int, lines))
    lines.sort()
    lines2 = copy.deepcopy(lines)
    lines3 = copy.deepcopy(lines2)
    for first in lines:
        first = int(first)
        for second in lines2:
            second = int(second)
            for third in lines3:
                third = int(third)
                if first+second+third == 2020:
                    print(first*second*third)
        del lines2[0]