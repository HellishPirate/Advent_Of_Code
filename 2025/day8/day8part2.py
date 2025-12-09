# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:40:24 2025

@author: diana
"""

import numpy as np
from collections import defaultdict

largestCircuits = 3

with open("day8.txt", "r") as f:
    day8in = f.readlines()
    
day8in = [item.strip() for item in day8in]
day8in = np.loadtxt(day8in, dtype=int, delimiter=",")

noOfConnections = 1000

pairs = []
dists = []
N = len(day8in)
for i in range(N):
    diffs = day8in[i] - day8in[i+1:]
    euclid = np.linalg.norm(diffs, axis=1)

    for k, dist in enumerate(euclid):
        j = i + 1 + k
        pairs.append((i, j))
        dists.append(dist)

pairs = np.array(pairs)
dists = np.array(dists)
while True:
    idx = np.argpartition(dists, noOfConnections)[:noOfConnections]
    minPairs = set(map(tuple, pairs[idx]))
        
    graph = defaultdict(list) 
    for edge in minPairs:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
        
    seen = set()
    components = []

    for node in graph:
        if node not in seen:
            stack = [node]
            comp = set()
            seen.add(node)
            
            while stack:
                curr = stack.pop()
                comp.add(curr)
                for neighbour in graph[curr]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
            components.append(comp)
    if len(seen) == N:
        break
    noOfConnections += 1

lastPairCoords = pairs[idx]
lastPairCoords = lastPairCoords[-1,:]
lastPairBoxes = day8in[lastPairCoords]
part2 = lastPairBoxes[0, 0] * lastPairBoxes[1, 0]

print("Day 8 Part 2: %d" %part2)