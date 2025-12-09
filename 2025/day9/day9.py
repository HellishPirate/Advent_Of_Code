# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 10:59:59 2025

@author: diana
"""

import numpy as np
from shapely import Polygon

with open("day9.txt", "r") as f:
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

i_idx, j_idx = np.triu_indices(N, k=1)
p1 = day9in[i_idx]
p2 = day9in[j_idx]

rectangles = np.hstack([np.minimum(p1, p2), np.maximum(p1, p2)])
areas = []
for x1, y1, x2, y2 in rectangles:
    areas.append((abs(x1 - x2)+1) * (abs(y1 - y2)+1))
    
fullPolygon = Polygon(day9in)
validAreas = []
for rectangleI, areaI in zip(rectangles, areas):
    xmin, ymin, xmax, ymax = rectangleI
    rect_poly = Polygon([(xmin, ymin),(xmin, ymax),(xmax, ymax),(xmax, ymin)])
    if rect_poly.within(fullPolygon) or rect_poly.covered_by(fullPolygon):
        validAreas.append(areaI)

largestValidArea = max(validAreas)
print("Day 9 Part 2: %d" %largestValidArea)