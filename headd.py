from sys import argv

def headd(fname):
    with open(fname) as file:
        lines = file.readlines()
        for line in lines[:10]:
            print(line, end='') 

if __name__ == '__main__':
    headd(argv[1])
