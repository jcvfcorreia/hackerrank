#!/bin/python3

import sys

n = int(input().strip())

b = "{0:b}".format(n)
c = 0
m = 0

for s in b:
    if s is '1':
        c += 1
        if c >= m:
            m = c
    else:
        c = 0

print(m)
