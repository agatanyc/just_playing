from sys import argv

def fac(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

if __name__ == '__main__':
    print(fac(int(argv[1])))
