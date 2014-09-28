from sys import argv

def square(n):
    """(int) -> int
    Return square value of the integer passed at the prompt.
    """
    r = 1
    x = int(input("Enter a number: "))
    r = x * x
    return r

if __name__ == '__main__':
    print(square(int(argv[1])))
