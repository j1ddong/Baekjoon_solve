from collections import deque

def BFS():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        ci, cj, v = q.popleft()
        if ci == N -1 and cj == M - 1:
            return visited[ci][cj][v]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][v]:
                if not arr[ni][nj]:
                    q.append((ni, nj, v))
                    visited[ni][nj][v] = visited[ci][cj][v] + 1
                elif arr[ni][nj] and v == 0:
                    q.append((ni, nj, 1))
                    visited[ni][nj][1] = visited[ci][cj][0] + 1
    return -1



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(BFS())