import sys

r = 0
for line in sys.stdin.readlines():
    r += len(line)
print(r)

