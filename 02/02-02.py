#!/usr/bin/env python

with open('input.txt', 'r', encoding='utf-8') as input:
    lines = []
    yes = 0
    no = 0
    for line in input:
        lines.append(line.rstrip())

    for i in lines:
        line = i.split(' ')
        pwrangelo = int(line[0].split('-')[0]) - 1
        pwrangehi = int(line[0].split('-')[1]) - 1
        pwletter = line[1].rstrip(':')
        pw = line[2]
        if (pw[pwrangelo] == pwletter and pw[pwrangehi] != pwletter):
            yes = yes + 1
        elif (pw[pwrangelo] != pwletter and pw[pwrangehi] == pwletter):
            yes = yes + 1
        else:
            no = no + 1
    print('yes: ' + str(yes) + ', no: ' + str(no))