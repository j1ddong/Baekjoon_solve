M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
resultArea = []

def colorArr(si, sj, ei, ej):
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 1

def dfs(si, sj):
    visited[si][sj] = 1
    stack = [(si, sj)]
    cnt = 0
    while stack:
        ci, cj = stack.pop()
        cnt += 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and not visited[ni][nj]:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
    return cnt

for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    colorArr(si, sj, ei, ej)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            area = dfs(i, j)
            resultArea.append(area)

resultArea.sort()

print(len(resultArea))
print(*resultArea)