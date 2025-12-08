# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 12:21:43 2025

@author: diana
"""

with open("day7.txt", "r") as f:
    day7in = f.readlines()
    
def dfs_split_count(startRow, startCol, grid):
    rows, cols = len(grid), len(grid[0])
    stack = [(startRow, startCol)]
    seen = set()
    splitCount = 0
    
    while stack:
        currentRow, currentCol = stack.pop()
        if not (0 <= currentRow < rows and 0 <= currentCol < cols):
            continue
        if (currentRow, currentCol) in seen:
            continue
        seen.add((currentRow, currentCol))
        cell = grid[currentRow][currentCol]
        if cell in ("S", "."):
            stack.append((currentRow+1, currentCol))
        elif cell == "^":
            stack.append((currentRow+1, currentCol+1))
            stack.append((currentRow+1, currentCol-1))
            splitCount += 1
            
    return splitCount

def dfs_path_count(startRow, startCol, grid):
    rows, cols = len(grid), len(grid[0])
    stack = [(startRow, startCol, False)]
    memo = {}
    
    while stack:
        currentRow, currentCol, processedChildrenFlag = stack.pop()
        if not (0 <= currentRow < rows and 0 <= currentCol < cols):
            memo[(currentRow, currentCol)] = 1
            continue
        if (currentRow, currentCol) in memo:
            continue
        cell = grid[currentRow][currentCol]
        
        if not processedChildrenFlag:
            stack.append((currentRow, currentCol, True))
            if cell in ("S", "."):
                stack.append((currentRow+1, currentCol, False))
            elif cell == "^":
                stack.append((currentRow+1, currentCol+1, False))
                stack.append((currentRow+1, currentCol-1, False))
            continue
        
        if cell in ("S", "."): # only gets here if possessedChildrenFlag is true
            memo[(currentRow, currentCol)] = memo.get((currentRow+1, currentCol), 0)
        elif cell == "^":
            left = memo.get((currentRow+1, currentCol-1), 0)
            right = memo.get((currentRow+1, currentCol+1), 0)
            memo[(currentRow, currentCol)] = left + right
    
    pathCount = memo.get((startRow, startCol), 0)
    return pathCount

startPosCol = day7in[0].index("S")

part1 = dfs_split_count(0, startPosCol, day7in)
print("Day 7 Part 1: %d" %part1)

part2 = dfs_path_count(0, startPosCol, day7in)
print("Day 7 Part 2: %d" %part2)
