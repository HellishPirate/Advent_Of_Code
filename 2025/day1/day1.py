# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 22:25:07 2025

@author: diana
"""

with open("day1.txt") as f:
    day1in = f.readlines()
dialNo = 50
count = 0

for i in range(len(day1in)):
    direction = day1in[i][0]
    turnDist = int(day1in[i][1:])
    if direction == "R":
        dialNo = (dialNo + turnDist)
    elif direction == "L":
        dialNo = (dialNo - turnDist)
    dialNo = dialNo % 100
    if dialNo == 0:
        count += 1

part1 = count
dialNo = 50
count = 0

for i in range(len(day1in)):
    direction = day1in[i][0]
    turnDist = int(day1in[i][1:])
    if direction == "R":
        for j in range(1, turnDist+1):
            dialNo = dialNo + 1
            dialNo = dialNo % 100
            if dialNo == 0:
                count += 1
    elif direction == "L":
        for k in range(1, turnDist+1):
            dialNo = dialNo - 1
            dialNo = dialNo % 100
            if dialNo == 0:
                count += 1

part2 = count
print("Day 1 Part 1: %d" %part1)
print("Day 1 Part 2: %d" %part2)