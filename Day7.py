#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr_r = arr[::-1]
out = ""

for s in range(len(arr_r)):
    out += "%s " % arr_r[s]

print(out)