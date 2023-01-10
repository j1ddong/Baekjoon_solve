from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[si][sj] = 1
    cnt = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 < ni <= N and 0 < nj <= N and not visited[ni][nj]:
                if road.get((ci, cj)) and (ni, nj) in road[(ci, cj)]:
                    continue
                if farm[ni][nj] == 1:
                    cnt += 1
                visited[ni][nj] = 1
                q.append((ni, nj))
    return cnt

N, K, R = map(int, input().split())
road = {}
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    if road.get((r1, c1)):
        road[(r1, c1)].append((r2, c2))
    else:
        road[(r1, c1)] = [(r2, c2)]
    if road.get((r2, c2)):
        road[(r2, c2)].append((r1, c1))
    else:
        road[(r2, c2)] = [(r1, c1)]

farm = [[0] * (N + 1) for _ in range(N + 1)]
si = sj = -1
ans, stand = 0, K - 1
cows = []
for _ in range(K):
    r, c = map(int, input().split())
    farm[r][c] = 1
    cows.append((r, c))

for si, sj in cows:
    ans += stand
    ans -= bfs(si, sj)
    farm[si][sj] = 0
    stand -= 1
print(ans)