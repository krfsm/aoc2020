#!/usr/bin/env python

with open('input.txt', 'r', encoding='utf-8') as input:
    all_lines = input.readlines()

trees = 0
positionx = 0
iterations = 1

for line in all_lines:

    curline = ''
    line = line.rstrip()

    for i in range(iterations):
        curline = curline + line

    linelist = list(curline)
    if linelist[positionx] == '#':
        linelist[positionx] = 'X'
        trees = trees + 1
    else:
        linelist[positionx] = 'O'
    positionx = positionx + 3

    if positionx >= len(curline):
        iterations = iterations + 1

print('A grand total of ' + str(trees) + ' trees were hit.')
