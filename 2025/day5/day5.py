print("\033[2J\033[H", end="", flush=True)
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:21:49 2025

@author: diana
"""
import numpy as np

day5in = open("day5.txt").readlines()
for i in range(len(day5in)):
    if len(day5in[i]) == 1:
        idx = i
        break
    
day5Ranges = day5in[0:idx]
day5IngredientIDs = day5in[idx+1:]

ranges = np.zeros((2, len(day5Ranges)))
    
for i in range(len(day5Ranges)):
    ranges[:, i] = np.fromstring(day5Ranges[i], sep="-")

count = 0
for i in range(len(day5IngredientIDs)):
    lowerRange = int(day5IngredientIDs[i]) >= ranges[0,:]
    upperRange = int(day5IngredientIDs[i]) <= ranges[1,:]
    checkAll = np.logical_and(lowerRange, upperRange)
    checkAny = np.any(checkAll)
    if checkAny:
        count += 1
        
print("Day 5 Part 1: %d" %count)

sortedRanges = np.sort(ranges)
mergedRange = np.zeros((2,0))
currRange = sortedRanges[:, [0]]
for i in range(1, len(ranges[1])):
    if currRange[1, 0] < sortedRanges[0, i]:
        mergedRange = np.column_stack((mergedRange, currRange))
        currRange = sortedRanges[:, [i]]
    else:
        currRange[1, 0] = max(currRange[1, 0], sortedRanges[1, i])
mergedRange = np.column_stack((mergedRange, currRange))

diffs = (mergedRange[1,:] - mergedRange[0,:]) + 1
count1 = sum(diffs)

print("Day 5 Part 2: %d" %count1)