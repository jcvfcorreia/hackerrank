def factorial(n=None):
    if n is not None:
        if n == 1:
            return 1
        else:
            return factorial(n-1)*n
    else:
        return 0

if __name__ == '__main__':
    N = int(input())
    print("%d" % factorial(N))