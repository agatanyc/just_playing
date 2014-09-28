import sys

def read_lines():
    input = sys.stdin.readlines()
    for line in input:
        e = len(line)
    return e

if __name__ == '__main__':
    print(read_lines())
