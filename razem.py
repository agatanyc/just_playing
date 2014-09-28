from sys import argv

for x in argv[1:]:
    print(x[::-1], end=' ')
print()
