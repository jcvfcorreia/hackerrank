n = int(input())

for i in range(n):
    s = input()
    k = 0
    odd = ""
    even = ""
    for j in s:
        if k % 2 is 0:
            odd += j
        else:
            even += j
        k += 1
    print("%s %s" % (odd, even))

