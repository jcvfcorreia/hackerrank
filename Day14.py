class Difference:
    maximumDifference = 0

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        aDiff = []
        for i in range(0, len(self.__elements)-1):
            for j in range(i+1, len(self.__elements)):
                dif = abs(self.__elements[i] - self.__elements[j])
                aDiff.append(dif)
        self.maximumDifference = sorted(aDiff, reverse=True)[0]

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
