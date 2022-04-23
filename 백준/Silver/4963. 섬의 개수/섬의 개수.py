def DFS(si, sj):
    stack = [(si, sj)]
    MAP[si][sj] = 0
    while stack:
        ci, cj = stack.pop()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < h and 0 <= nj < w and MAP[ni][nj]:
                stack.append((ni, nj))
                MAP[ni][nj] = 0


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                DFS(i, j)
                ans += 1
    print(ans)
