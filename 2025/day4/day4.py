print("\033[2J\033[H", end="", flush=True)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 12:53:50 2025

@author: diana
"""

import numpy as np
import scipy as sc

day4in = open("day4.txt").readlines()
for i in range(len(day4in)):
    day4in[i] = day4in[i].strip()
day4in = [[ord(c) for c in s] for s in day4in]
day4in = np.asarray(day4in)
day4in = (day4in == 64).astype(int)

adjMat = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

allNeighbourCount = sc.signal.convolve2d(day4in, adjMat, mode="same")
allNeighbourCount = allNeighbourCount.astype(float)
allNeighbourCount[day4in == 0] = np.nan
accessiblePaper = allNeighbourCount < 4
count = day4in[accessiblePaper]
count = sum(count)
        
print("Day 4 Part 1: %d" %count)

anyAccessiblePaper = accessiblePaper.any()
count1 = 0
while anyAccessiblePaper:
    allNeighbourCount = sc.signal.convolve2d(day4in, adjMat, mode="same")
    allNeighbourCount = allNeighbourCount.astype(float)
    allNeighbourCount[day4in == 0] = np.nan
    accessiblePaper = allNeighbourCount < 4
    count = day4in[accessiblePaper]
    count = len(count)
    if count == 0:
        break
    count1 = count1 + count 
    day4in[accessiblePaper] -= 1
    anyAccessiblePaper = accessiblePaper.any()
    
print("Day 4 Part 2: %d" %count1)