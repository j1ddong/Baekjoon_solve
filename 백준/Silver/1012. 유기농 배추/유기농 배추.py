T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    def dfs(si, sj):
        visited[si][sj] = 1
        stack = [(si, sj)]
        while stack:
            ci, cj = stack.pop()
            for di, dj in[(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        stack.append((ni, nj))

    result = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)