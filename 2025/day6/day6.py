# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:13:22 2025

@author: diana
"""

import numpy as np

with open("day6.txt", "r") as f:
    day6in = f.readlines()
    
operationsWithSpaces = day6in[-1]
operations = "".join(operationsWithSpaces.split())
day6in = day6in[:-1]
mathHomework = np.loadtxt(day6in)

count = 0
for i in range(len(operations)):
    match operations[i]:
        case "*":
            result = np.prod(mathHomework[:,i])
        case "+":
            result = sum(mathHomework[:,i])
    count += result
    
print("Day 6 Part 1: %d" %count)

numStack = []
correctedMathHomework = []
row, col = np.shape(mathHomework)
for i in range(len(day6in[0])):
    if i < len(operationsWithSpaces)-1:
        if (operationsWithSpaces[i+1] == "*" or operationsWithSpaces[i+1] == "+"):
            numStack = " ".join(numStack)
            numStack = numStack.strip()
            correctedMathHomework.append(numStack)
            numStack = []
            continue
    numList = [item[i] for item in day6in]
    numList = "".join(numList)
    numStack.append(numList)

numStack = " ".join(numStack)
numStack = numStack.strip()
correctedMathHomework.append(numStack)

count = 0
for i in range(len(operations)):
    correctedMathHomeworkCol = np.loadtxt([correctedMathHomework[i]])
    match operations[i]:
        case "*":
            result = np.prod(correctedMathHomeworkCol)
        case "+":
            result = sum(correctedMathHomeworkCol)
    count += result
    
print("Day 6 Part 2: %d" %count)