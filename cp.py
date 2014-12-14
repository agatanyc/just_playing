from sys import argv

def cp(n):
    r = []
    for i in range(n +1):
        if i % 15 == 0:
            r.append("caraclepop")
        elif i % 5 == 0:
            r.append("crackle")
        elif i % 3 == 0:
            r.append("pop")
        else:
            r.append(i)
    return r 

if len(argv) > 1:
    n = int(argv[1])
else:
    n = 100
print(cp(n))

