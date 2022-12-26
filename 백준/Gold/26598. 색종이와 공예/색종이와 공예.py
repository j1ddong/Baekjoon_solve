from collections import deque

def check_length(si, sj):
    global visited
    li = ri = si
    lj = rj = sj
    standard = lst[si][sj]
    queue = deque([(si, sj)])
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if lst[ni][nj] == standard:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    li, lj, ri, rj = min(ni, li), min(lj, nj), max(ri, ni), max(rj, nj)
    return (li, lj, ri, rj)

def is_rectangle(li, lj, ri, rj, si, sj):
    global visited
    standard = lst[si][sj]
    for i in range(li, ri + 1):
        for j in range(lj, rj + 1):
            visited[i][j] = 1
            if lst[i][j] != standard:
                return False
    return True

def sol():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = 1
                li, lj, ri, rj = check_length(i, j)
                if not is_rectangle(li, lj, ri, rj, i, j):
                    return False
    return True

N, M = map(int, input().split())
lst = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

if sol():
    print('dd')
else:
    print('BaboBabo')