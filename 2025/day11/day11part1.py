# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 13:40:33 2025

@author: diana
"""

import re
import networkx as nx

with open("day11.txt", "r") as f:
    day11in = f.readlines() 
   
directedGraph = {}

for i in range(len(day11in)):
    node = re.findall(r"^.*?(?=-|:)", day11in[i])
    edges = re.findall(r":(.*)", day11in[i])
    edges = edges[0].split()
    directedGraph[node[0]] = edges
    
nxGraph = nx.DiGraph(directedGraph)
targets = [node for node, edges in nxGraph.edges() if "out" in edges]

noOfPaths = 0
for target in targets:
    if not nx.has_path(nxGraph, "you", target):
        continue
    for path in nx.all_simple_paths(nxGraph, source="you", target=target):
        noOfPaths += 1
        
print("Day 11 Part 1: %d" %noOfPaths)

