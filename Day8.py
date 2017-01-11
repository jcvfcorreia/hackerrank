n = int(input())

dict = {}
for i in range(n):
    s = input().split(' ')
    dict.update({s[0]: s[1]})

o = True
while o:
    s = input()
    if s != '':
        try:
            print("%s=%s" % (s, dict[s]))
        except KeyError:
            print('Not found')
    else:
        o = False