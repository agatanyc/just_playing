import sys

def sum_2():
    inputs = sys.stdin.read().split()
    r = 0
    for i in inputs:
        r += int(i)
    return r

if __name__ == '__main__':
    print(sum_2())
