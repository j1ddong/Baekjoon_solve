from itertools import combinations
from copy import deepcopy

def yes_or_no(block, lst):
    for bi, bj in block:
        lst[bi][bj] = 'O'
    for ti, tj in teacher:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ti + di, tj + dj
            while 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == 'O':
                    break
                elif lst[ni][nj] == 'S':
                    return True
                ni, nj = ni + di, nj + dj
    return False

N = int(input())
arr = [list(input().split()) for _ in range(N)]
empty = []
teacher = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            empty.append((i, j))
        elif arr[i][j] == 'T':
            teacher.append((i, j))

combi = combinations(empty, 3)
flag = False
for elem in combi:
    if not yes_or_no(elem, deepcopy(arr)):
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
