from sys import argv

print(' '.join(x[::-1] for x in argv[1:]))
