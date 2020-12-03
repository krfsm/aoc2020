#!/usr/bin/env python

xlist = [1, 3, 5, 7, 1]
ylist = [1, 1, 1, 1, 2]
totaltrees = 1

with open('input.txt', 'r', encoding='utf-8') as input:
    all_lines = input.readlines()

for i in range(5):
    x = xlist[i]
    y = ylist[i]

    trees = 0
    posx = 0
    posy = 0

    iterations = 1
    for line in all_lines:
        if y == 2 and posy % 2 == 1:
            posy = posy + 1
        else:
            curline = ''
            line = line.rstrip()
            for iter in range(iterations):
                curline = curline + line
            linelist = list(curline)
            if linelist[posx] == '#':
                linelist[posx] = 'X'
                trees = trees + 1
            else:
                linelist[posx] = 'O'
            posx = posx + x
            if posx >= len(curline):
                iterations = iterations + 1
            posy = posy + 1
    totaltrees = totaltrees * trees
    print('Iteration ' + str(i+1) + ' trees: ' + str(trees))
    if i < 4:
        print('Total trees so far: ' + str(totaltrees))
print('Total trees: ' + str(totaltrees))
