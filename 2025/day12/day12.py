# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 14:57:02 2025

@author: diana
"""

import re
import numpy as np

with open("day12.txt", "r") as f:
    day12in = f.readlines()
    
for i in range(len(day12in)):
    if "x" in day12in[i]:
        presentShapes = day12in[:i]
        regions = day12in[i:]
        break
    
presentShapes = [i for i in presentShapes if i != "\n"]
presentShapesOnly = [i for i in presentShapes if not re.search(r"\d", i)]
n = 3
presentShapesOnly = ["".join(presentShapesOnly[i:i+n]) for i in range(0, len(presentShapesOnly), n)]
presentShapesOnly = [i.replace("\n", "") for i in presentShapesOnly]
presentShapesOnly = [i.rstrip() for i in presentShapesOnly]
presentShapesOnly = [i.replace("#", "1") for i in presentShapesOnly]
presentShapesOnly = [i.replace(".", "0") for i in presentShapesOnly]

areas = []
for i in range(len(presentShapesOnly)):
    area = 0
    for j in presentShapesOnly[i]:
        if j == "1":
            area += 1
    areas.append(area)
    
gridAreas = []
noOfPresents = []
for i in range(len(regions)):
    gridArea = re.findall(r"^.*?(?=-|:)", regions[i])
    noOfPresentsInRegion = re.findall(r":(.*)", regions[i])
    noOfPresents.append(noOfPresentsInRegion[0])
    gridAreas.append(gridArea[0])
    
gridAreas = [i.replace("x", "*") for i in gridAreas]
gridAreas = [eval(i) for i in gridAreas]
gridAreas = np.array(gridAreas)

areas = np.array(areas)
noOfPresents = np.loadtxt(noOfPresents)

presentsInGrid = []
for i in range(len(noOfPresents)):
    presentsInGrid.append(areas @ noOfPresents[i])
    
part1 = np.sum(presentsInGrid <= gridAreas)

print("Day 12 Part 1: %d" %part1)
