# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 10:59:59 2025

@author: diana
"""

import numpy as np

with open("day9sample.txt", "r") as f:
    day9in = f.readlines()
    
day9in = [item.strip() for item in day9in]
day9in = np.loadtxt(day9in, dtype=int, delimiter=",")

N = len(day9in)
currMaxVal = 0
for i in range(N):
    xLength = abs(day9in[i,0] - day9in[:,0]) + 1
    yLength = abs(day9in[i,1] - day9in[:,1]) + 1
    area = xLength * yLength
    areaMax = max(area)
    if areaMax > currMaxVal:
        currMaxVal = areaMax
        
print("Day 9 Part 1: %d" %currMaxVal)

