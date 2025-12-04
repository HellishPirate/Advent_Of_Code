print("\033[2J\033[H", end="", flush=True)
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 06:41:12 2025

@author: diana
"""

day2in = open("day2.txt").readlines()
day2in = day2in[0].split(",")
invalidIDCount = 0

for i in range(len(day2in)):
    rangeofIDs = day2in[i].split("-")
    minID = int(rangeofIDs[0])
    maxID = int(rangeofIDs[-1])
    
    for j in range(minID, maxID+1):
        ID = str(j)
        lenID = len(ID)
        if lenID % 2 == 0:
            if ID[0:lenID//2] == ID[lenID//2:]:
                invalidIDCount = invalidIDCount + j
                
print("Day 2 Part 1: %d" %invalidIDCount)                

invalidIDCount = 0

for i in range(len(day2in)):
    rangeofIDs = day2in[i].split("-")
    minID = int(rangeofIDs[0])
    maxID = int(rangeofIDs[-1])
    
    for j in range(minID, maxID+1):
        ID = str(j)
        concatID = ID + ID 
        concatID = concatID[1:-1]
        if ID in concatID:
            invalidIDCount = invalidIDCount + j
            
print("Day 2 Part 2: %d" %invalidIDCount)
                
