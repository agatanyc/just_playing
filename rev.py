from sys import argv

def rev(fname):
    with open(fname) as file:
        lines = file.readlines()

    r = ""
    for line in lines:
        r += line[::-1]
    return r

if __name__ == '__main__':
    print(rev(argv[1]))
