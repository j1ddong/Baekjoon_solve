import sys
from collections import deque
input = sys.stdin.readline

def find_usado(node):
    q = deque([(node, INF)])
    visited = [False] * (N + 1)
    visited[node] = True
    ans = 0

    while q:
        cnode, min_num = q.popleft()
        for nnode, ndistance in graph[cnode]:
            usado = min(min_num, ndistance)
            if usado >= k and not visited[nnode]:
                q.append((nnode, usado))
                visited[nnode] = True
                ans += 1
    return ans


N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = 1e9 + 1
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, idx = map(int, input().split())
    print(find_usado(idx))