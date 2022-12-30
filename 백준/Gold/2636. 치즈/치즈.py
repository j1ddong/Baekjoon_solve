def melting():
    q = [(0, 0)]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    cheese = []

    while q:
        ci, cj = q.pop()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if MAP[ni][nj]:
                    cheese.append((ni, nj))
                else:
                    q.append((ni, nj))
    return cheese

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = cnt = 0

cnt = sum([sum(MAP[i]) for i in range(N)])

while True:
    cheese = melting()
    ans += 1
    if cnt - len(cheese) == 0:
        break
    cnt -= len(cheese)
    for i, j in cheese:
        MAP[i][j] = 0

print(ans)
print(cnt)