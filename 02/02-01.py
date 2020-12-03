#!/usr/bin/env python

with open('input.txt', 'r', encoding='utf-8') as input:
    lines = []
    yes = 0
    no = 0
    for line in input:
        lines.append(line.rstrip())

    for i in lines:
        line = i.split(' ')
        pwrange = line[0]
        pwletter = line[1].rstrip(':')
        pw = line[2]
        count = int(pw.count(pwletter))
        pwminmaxrange = pwrange.split('-')
        if int(pwminmaxrange[0]) <= count <= int(pwminmaxrange[1]):
            yes = yes + 1
        else:
            no = no + 1
    print('yes: ' + str(yes) + ', no: ' + str(no))