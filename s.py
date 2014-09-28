from sys import argv

def s(fname):
    with open(fname) as file:
        ss = file.readlines()
        ss.sort()
        for line in ss:
            print(line, end='')
        return ss

if __name__ == '__main__':
    print(s(argv[1]))
