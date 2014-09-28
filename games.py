import random

def game(n):
    r = random.randrange(1, n)
    while True:
        x = int(input("Guess the number: "))
        if x > r:
            print("Too high!")
        elif x < r:
            print("Too low!")
        else:
            print("SUCCESS!!!")
            return

if __name__== '__main__':
    game(101)
