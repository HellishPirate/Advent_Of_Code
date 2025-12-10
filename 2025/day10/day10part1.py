# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:13:02 2025

@author: diana
"""

import re
import numpy as np
import itertools
        
with open("day10.txt", "r") as f:
    day10in = f.readlines()
    
indicatorLights = []
N = len(day10in)
for i in range(N):
    indicatorLights.append(re.findall(r"\[(.*?)\]", day10in[i]))
    
rStack = []

for i in range(N):
    buttonSchematic = re.findall(r"\((.*?)\)", day10in[i]) # i
    noOfLights = len(indicatorLights[i][0]) # i 0
    indicatorLightsI = re.sub(r"#", "1", indicatorLights[i][0]) # i 0
    indicatorLightsI = re.sub(r"\.", "0", indicatorLightsI)
    target = np.frombuffer(indicatorLightsI.encode("ascii"), dtype="S1").astype(int)
    rangeOfButtons = np.arange(noOfLights)

    rowsStack = np.zeros((0, noOfLights))
    for j in range(len(buttonSchematic)):
        buttonsPressed = buttonSchematic[j].split(",") # j
        buttonsPressed = np.array(buttonsPressed, dtype=int)

        binaryVec = np.isin(rangeOfButtons, buttonsPressed)
        binaryVec = binaryVec.astype(int)
        rowsStack = np.vstack([rowsStack, binaryVec])

    r = 0
    while True:
        r += 1
        allCombos = itertools.combinations(range(len(rowsStack)), r)

        for combo in allCombos:
            xorVec = np.logical_xor.reduce(rowsStack[list(combo)], axis=0)
            if np.all(xorVec == target):
                break
        if np.all(xorVec == target):
            break
    rStack.append(r)
    
part1 = sum(rStack)
print("Day 10 Part 1: %d" %part1)