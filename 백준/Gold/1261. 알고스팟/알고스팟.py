from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

check = [[10001] * M for _ in range(N)]
check[0][0] = 0

def dijkstra():
    q = deque([(0, 0)])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if check[ni][nj] > check[ci][cj] + arr[ni][nj]:
                    check[ni][nj] = check[ci][cj] + arr[ni][nj]
                    q.append((ni, nj))

dijkstra()
print(check[-1][-1])