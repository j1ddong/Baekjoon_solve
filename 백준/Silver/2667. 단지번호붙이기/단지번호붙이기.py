def DFS(si, sj):
    stack = [(si, sj)]
    MAP[si][sj] = 0
    cnt = 1
    while stack:
        ci, cj = stack.pop()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj]:
                stack.append((ni, nj))
                MAP[ni][nj] = 0
                cnt += 1
    return cnt


N = int(input())

arr = [input() for _ in range(N)]
MAP = [[]for _ in range(N)]
for i in range(N):
    for j in range(N):
        MAP[i].append(int(arr[i][j]))

ans = 0
result = []
for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            result.append((DFS(i, j)))
            ans += 1
print(ans)
for ele in sorted(result):
    print(ele)
