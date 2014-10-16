r = 0
print(r)
s = input('> ').strip()
while s:
    op, n = s[0], int(s[1:]) 
    if op == '-':
        r -= n
    elif op == '+':
        r += n
    elif op == '*':
        r *= n
    elif op == '/':
        r /= n
    else:
        print("Bad operator:", op)
    print(r)
    s = input('> ').strip()
