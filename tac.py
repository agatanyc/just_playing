from sys import argv

def tac(fname):
    with open(fname) as file:
        s = file.readlines()
    return ''.join(s[::-1])

if __name__ == '__main__':
    print(tac(argv[1]))

