from collections import deque

def bfs(start, end):
    q = deque([(start, 0)])
    visited = [0] * (N + 1)
    visited[start] = 1
    while q:
        now, distance = q.popleft()
        if now == end:
            print(distance)
            return
        for next, w in graph[now]:
            if not visited[next]:
                q.append((next, distance + w))
                visited[next] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))
for _ in range(M):
    s, e = map(int, input().split())
    bfs(s, e)