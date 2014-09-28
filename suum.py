import sys

def suum():
    inputs = sys.stdin.read().split()
    r = 0
    for s in inputs:
        r += int(s)
    return r

if __name__ == '__main__':
    print(suum())
