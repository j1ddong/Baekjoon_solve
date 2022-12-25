import math

def spread(lst):
    new = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j] > 0:
                cnt = 0
                amount = math.floor(MAP[i][j] / 5)
                for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and MAP[ni][nj] != -1:
                        cnt += 1
                        new[ni][nj] += amount
                remain = MAP[i][j] - amount * cnt
                if cnt:
                    new[i][j] += remain
    return new

def air_cleaner(lst):
    origin, lst[air1i][1] = lst[air1i][1], 0
    for j in range(2, C):
        lst[air1i][j], origin = origin, lst[air1i][j]
    for i in range(air1i - 1, -1, -1):
        lst[i][C - 1], origin = origin, lst[i][C - 1]
    for j in range(C - 2, -1, -1):
        lst[0][j], origin = origin, lst[0][j]
    for i in range(1, air1i):
        lst[i][0], origin = origin, lst[i][0]
    
    origin, lst[air2i][1] = lst[air2i][1], 0
    for j in range(2, C):
        lst[air2i][j], origin = origin, lst[air2i][j]
    for i in range(air2i + 1, R):
        lst[i][C - 1], origin = origin, lst[i][C - 1]
    for j in range(C - 2, -1, -1):
        lst[-1][j], origin = origin, lst[-1][j]
    for i in range(R - 2, air2i, -1):
        lst[i][0], origin = origin, lst[i][0]
    return lst

R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
air1i = air2i = ans = 0
for i in range(R):
    if MAP[i][0] == -1:
        air1i = i
        air2i = i + 1
        break

for _ in range(T):
    MAP = spread(MAP)
    MAP[air1i][0] = MAP[air2i][0] = -1
    MAP = air_cleaner(MAP)

for i in range(R):
    for j in range(C):
        if MAP[i][j] > 0:
            ans += MAP[i][j]
print(ans)