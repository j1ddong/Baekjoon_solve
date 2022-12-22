def check(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if restroom[i][j]:
                return False
    return True

def main(x, y, size):
    global num
    num += 1
    ns = size // 2
    if check(x, y, ns):
        restroom[x + ns - 1][y + ns - 1] = num
    if check(x, y + ns, ns):
        restroom[x + ns - 1][y + ns] = num
    if check(x + ns, y, ns):
        restroom[x + ns][y + ns - 1] = num
    if check(x + ns, y + ns, ns):
        restroom[x + ns][y + ns] = num
    if size == 2:
        return 
    main(x, y, ns)
    main(x, y + ns, ns)
    main(x + ns, y, ns)
    main(x + ns, y + ns, ns)


K = int(input())
x, y = map(int, input().split())

length = 2 ** K
holeX, holeY = length - y, x - 1
restroom = [[0] * length for _ in range(length)]
restroom[holeX][holeY] = -1

num = 0
main(0, 0, length)
for elem in restroom:
    print(*elem)