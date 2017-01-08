#!/bin/python3

import sys


n = int(input().strip())
i = 1
while i <= 10:
    print("%s x %s = %s" % (str(n), str(i) , str(n * i)))
    i += 1