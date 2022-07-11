import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
    q = deque([node])
    visited[node] = 1
    while q:
        cnode = q.popleft()
        for nnode in graph[cnode]:
            if not visited[nnode]:
                q.append(nnode)
                visited[nnode] = cnode



N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(1)
for elem in visited[2:]:
    print(elem)
