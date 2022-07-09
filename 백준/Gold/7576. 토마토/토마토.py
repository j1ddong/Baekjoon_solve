from collections import deque


def BFS():
    q = deque(tomato)
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] and not visited[ni][nj]:                  
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))  


def result():
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                ans = max(ans, visited[i][j])
            elif visited[i][j] == 0:
                return -1 
    return ans - 1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tomato = []
visited = [[0] * M for _ in range(N)]
# 토마토 있는 곳 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i, j))
            visited[i][j] = 1
        elif arr[i][j] == -1:
            visited[i][j] = -1
BFS()
print(result())