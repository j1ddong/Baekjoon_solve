import math
from collections import deque

def union(i, j):
    global visited
    open = []
    sub_sum = map[i][j]
    queue = deque([[i, j]])
    while queue:
        ci, cj = queue.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and S <= abs(map[ci][cj] - map[ni][nj]) <= E:
                if not visited[ni][nj]:
                    open.append([ni, nj])
                    sub_sum += map[ni][nj]
                    queue.append([ni, nj])
                    visited[ni][nj] = 1
    return (open, sub_sum)

N, S, E = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                open, sub_sum = union(i, j)
                if open:
                    open.append([i, j])
                    new_sum = math.floor(sub_sum / len(open))
                    flag = True
                    for i, j in open:
                        map[i][j] = new_sum
    if not flag:
        break
    else:
        cnt += 1

print(cnt)