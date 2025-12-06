# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 13:05:56 2025

@author: diana
"""

with open("day3.txt") as f:
    day3in = f.readlines()
totalJoltage = 0

for i in range(len(day3in)):
    batteryPack = day3in[i].strip()
    maxBatteryVal = max(batteryPack[:-1]) # ignore last value
    maxBatteryValIdx = batteryPack.find(maxBatteryVal)
    secondMaxBatteryVal = max(batteryPack[maxBatteryValIdx+1:])
    joltage = maxBatteryVal + secondMaxBatteryVal
    totalJoltage = totalJoltage + int(joltage)
print("Day 3 Part 1: %d" %totalJoltage)

totalJoltage = 0
batteryPackLength = 12
for i in range(len(day3in)):
    batteryPack = day3in[i].strip()
    freeDigits = len(batteryPack) - batteryPackLength
    jolted1 = ""
    j = 1
    while freeDigits != 0 and j <= batteryPackLength:
        j += 1
        test = batteryPack[:freeDigits+1]
        maxBatteryVal = max(batteryPack[:freeDigits+1])
        maxBatteryValIdx = batteryPack.find(maxBatteryVal)
        freeDigits = freeDigits - maxBatteryValIdx
        batteryPack = batteryPack[maxBatteryValIdx+1:]
        jolted1 = jolted1 + maxBatteryVal
    lengthRemaining = batteryPackLength - len(jolted1)
    jolted2 = batteryPack[:lengthRemaining]
    joltage = jolted1 + jolted2
    totalJoltage = totalJoltage + int(joltage)
    
print("Day 3 Part 2: %d" %totalJoltage)