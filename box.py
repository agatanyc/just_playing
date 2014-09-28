from sys import argv

def line(n, p, h):
    print(p + (n * h) + p)

if __name__ == '__main__':
    n = int(argv[1])
    line(n, '+', '-')
    for i in range(n):
        line(n, '|', ' ')
    line(n, '+', '-')
