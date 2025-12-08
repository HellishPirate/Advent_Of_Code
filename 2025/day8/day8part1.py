# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 10:45:03 2025

@author: diana
"""

import numpy as np
from collections import defaultdict

noOfConnections = 1000
largestCircuits = 3

with open("day8.txt", "r") as f:
    day8in = f.readlines()
    
day8in = [item.strip() for item in day8in]
day8in = np.loadtxt(day8in, dtype=int, delimiter=",")

pairs = []
dists = []
N = len(day8in)
for i in range(N):
    diffs = day8in[i] - day8in[i+1:]
    euclid = np.linalg.norm(diffs, axis=1)

    for k, dist in enumerate(euclid):
        j = i + 1 + k # (i, i+1,2,3...)
        pairs.append((i, j))
        dists.append(dist)

pairs = np.array(pairs)
dists = np.array(dists)
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
        
lenOfComponents = []
for i in range(len(components)):
    lenOfComponents.append(len(components[i]))
lenOfComponents.sort(reverse=True)
part1 = np.prod(lenOfComponents[:largestCircuits])

print("Day 8 Part 1: %d" %part1)