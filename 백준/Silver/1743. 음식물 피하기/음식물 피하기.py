N, M, K = map(int, input().split())
trash = [list(map(int, input().split())) for _ in range(K)]
visited = [[0] * M for _ in range(N)]
ans = 0
for i, j in trash:
    if not visited[i - 1][j - 1]:
        stack = [(i, j)]
        visited[i - 1][j - 1] = 1
        cnt = 1
        while stack :
            si, sj = stack.pop()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = si + di, sj + dj
                if 0 < ni < N + 1 and 0 < nj < M + 1 and not visited[ni - 1][nj - 1] and [ni, nj] in trash:
                    stack.append((ni, nj))
                    cnt += 1
                    visited[ni - 1][nj - 1] = 1
        ans = max(ans, cnt)

print(ans)