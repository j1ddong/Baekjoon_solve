from collections import deque

def divide_turn(num):
    new = [[0] * N for _ in range(N)]
    for i in range(0, N, num):
        for j in range(0, N, num):
            for k in range(num):
                for l in range(num):
                    new[i + l][j + num - k - 1] = lst[i + k][j + l]

    melt = []
    for i in range(N):
        for j in range(N):
            if not new[i][j]:
                continue
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and new[ni][nj]:
                    cnt += 1
            if cnt < 3:
                melt.append((i, j))
    
    for i, j in melt:
        new[i][j] -= 1

    return new

def area(si, sj):
    cnt = 1
    q = deque([(si, sj)])
    visited[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and lst[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt

n, Q = map(int, input().split())
N = 2 ** n
lst = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
big_area = 0

for order in orders:
    lst = divide_turn(2 ** order)

ices = sum([sum(elem) for elem in lst])
visited = [[0] * N for _  in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][j] and not visited[i][j]:
            big_area = max(area(i, j), big_area)

print(ices)
print(big_area)