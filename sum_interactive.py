def sum_interactive():
    r = 0
    s = input("+ ").strip()
    while s != 'q':
        if s:
            r += int(s)
        else:
            print(r)
        s = input("+ ").strip()
    print(r)
            
if __name__ == '__main__':
    sum_interactive()
