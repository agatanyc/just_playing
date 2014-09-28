from sys import argv
import sys

def repeat():
    input = sys.stdin.read()
    if len(argv) > 1:
        print(input * int(argv[1]), end='')
    else:
        print(input)
if __name__ == '__main__':
    repeat()
