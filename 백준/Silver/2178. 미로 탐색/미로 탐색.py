from collections import deque


N, M = map(int, input().split())
arr = []

for _ in range(N):
    tempString = input()
    tempArr = []
    for temp in tempString:
        tempArr.append(int(temp))
    arr.append(tempArr)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0] * M for _ in range(N)]

def bfs(si, sj, cnt):
    q = deque([(si, sj, cnt)])
    visited[si][sj] = 1
    result = N * M + 1

    while q:
        ci, cj, cnt = q.popleft()
        cnt += 1
        if ci == N - 1 and cj == M - 1:
            result = min(cnt, result)
        for i in range(4):
            ni, nj = ci + dx[i], cj + dy[i]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    q.append((ni, nj, cnt))
                    visited[ni][nj] = 1
    return result


result = bfs(0, 0, 0)
print(result)