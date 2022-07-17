A, B = map(int, input().split())
cntl = cntr = 0
while True:
    if A > B:
        A = A - B
        cntl += 1
    elif A < B:
        B = B - A
        cntr += 1
    else:
        break

print(cntl, cntr)