from collections import deque

def BFS():
    q = deque(tomato)
    while q:
        ci, cj, ck = q.popleft()
        for di, dj, dk in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]:
            ni, nj, nk = ci + di, cj + dj, ck + dk
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and not arr[ni][nj][nk] and not visited[ni][nj][nk]:
                visited[ni][nj][nk] = visited[ci][cj][ck] + 1
                q.append((ni, nj, nk))


def result():
    ans = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == 0:
                    return -1
                ans = max(visited[i][j][k], ans)
    return ans - 1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
tomato = []
flag = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                tomato.append((i, j, k))
                visited[i][j][k] = 1
            elif arr[i][j][k] == -1:
                visited[i][j][k] = -1
            else:
                flag = 1
if flag == 0:
    print(0)
else:
    BFS()
    print(result())