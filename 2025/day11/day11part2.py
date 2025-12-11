# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 18:20:35 2025

@author: diana
"""

import re
import networkx as nx

def countPathsDAG(G, source, target):
    order = list(nx.topological_sort(G))
    dp = {n: 0 for n in G.nodes()}
    dp[source] = 1

    for u in order:
        for v in G.successors(u):
            dp[v] += dp[u]

    return dp[target]

with open("day11.txt", "r") as f:
    day11in = f.readlines() 
   
directedGraph = {}

for i in range(len(day11in)):
    node = re.findall(r"^.*?(?=-|:)", day11in[i])
    edges = re.findall(r":(.*)", day11in[i])
    edges = edges[0].split()
    directedGraph[node[0]] = edges
    
nxGraph = nx.DiGraph(directedGraph)

pathsSVR_FFT = countPathsDAG(nxGraph, "svr", "fft")
pathsFFT_DAC = countPathsDAG(nxGraph, "fft", "dac")
pathsDAC_Out = countPathsDAG(nxGraph, "dac", "out")
total = pathsSVR_FFT * pathsFFT_DAC * pathsDAC_Out
# there are never any paths from DAC to FFT (which makes sense as FFTs use digital data)

print("Day 11 Part 2: %d" %total)