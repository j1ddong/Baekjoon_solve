from collections import deque

# 가로 M, 세로 N
M, N = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
visited = [[0]*M for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_day = 0

def bfs(index):
    global max_day
    queue = deque(index)
    while queue:
        ci, cj, level = queue.popleft()
        for i in range(4):
            ni = ci + dx[i]
            nj = cj + dy[i]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    queue.append([ni, nj, level + 1])
                    visited[ni][nj] = 1
                    max_day = max(level+1, max_day)


ind = []
cnt = 0 # 토마토 다 익은지 확인 -1 and 1
cnt1 = 0 # 토마토가 전부 안익은 상태인지 확인 -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: # 익은 토마토면
            ind.append([i, j, 0])
            visited[i][j] = 1
            cnt += 1
        if arr[i][j] == -1:
            visited[i][j] = -1
            cnt += 1
            cnt1 += 1

bfs(ind)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            max_day = -1

if cnt == M*N: # 모든 토마토가 다 익은 상태
    max_day = 0

print(max_day)