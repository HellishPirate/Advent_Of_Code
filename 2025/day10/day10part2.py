# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:13:18 2025

@author: diana
"""

import re
import numpy as np
from scipy import optimize

with open("day10.txt", "r") as f:
    day10in = f.readlines()
    
buttonPresses = []
N = len(day10in)

for i in range(N):
    joltageVals = re.findall(r"\{(.*?)\}", day10in[i])
    joltageVals = np.loadtxt(joltageVals, dtype=int, delimiter=",")
    buttonSchematic = re.findall(r"\((.*?)\)", day10in[i])

    indicatorLights = (re.findall(r"\[(.*?)\]", day10in[i]))
    noOfLights = len(indicatorLights[0])

    rowsStack = np.zeros((0, noOfLights))
    rangeOfButtons = np.arange(noOfLights)
    for j in range(len(buttonSchematic)):
        buttonsPressed = buttonSchematic[j].split(",")
        buttonsPressed = np.array(buttonsPressed, dtype=int)

        binaryVec = np.isin(rangeOfButtons, buttonsPressed)
        binaryVec = binaryVec.astype(int)
        rowsStack = np.vstack([rowsStack, binaryVec])
        
    rowsStack = rowsStack.T
    coeffs = np.ones(len(buttonSchematic))
    constraint = optimize.LinearConstraint(rowsStack, joltageVals, joltageVals)
    integrality = coeffs.astype(int)
    res = optimize.milp(c=coeffs, constraints=constraint, integrality=integrality)
    buttonPresses.append(sum(res.x))
    
part2 = sum(buttonPresses)
print("Day 10 Part 2: %d" %part2)