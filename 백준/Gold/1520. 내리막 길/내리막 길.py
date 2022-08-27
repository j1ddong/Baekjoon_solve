import sys
sys.setrecursionlimit(10 ** 6)


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]

def dfs(ci, cj):
    if ci == M - 1 and cj == N - 1:
        return 1

    if visited[ci][cj] != -1:
        return visited[ci][cj]
    
    visited[ci][cj] = 0

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[ci][cj]:
            visited[ci][cj] += dfs(ni, nj)
    return visited[ci][cj]

print(dfs(0, 0))

