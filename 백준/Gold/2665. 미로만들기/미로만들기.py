from collections import deque

def dijkstra(N, lst):
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp = 0
                if lst[ni][nj] == 0:
                    temp += 1
                if visited[ni][nj] > visited[ci][cj] + temp:
                    visited[ni][nj] = visited[ci][cj] + temp
                    q.append((ni, nj))
    return visited[N - 1][N - 1]




N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
INF = 9999999999
visited = [[INF] * N for _ in range(N)]
ans = dijkstra(N, arr)
print(ans)